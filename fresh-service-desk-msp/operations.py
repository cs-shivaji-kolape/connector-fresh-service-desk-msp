"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
import json
from os.path import join
import requests
from connectors.core.connector import get_logger, ConnectorError
from connectors.cyops_utilities.builtins import download_file_from_cyops
from integrations.crudhub import make_request
import base64
import urllib.parse
from .constants import STATUS_MAP, PRIORITY_MAP, ERROR_MSGS
logger = get_logger('fresh-service-desk-msp')

class FreshService(object):
    def __init__(self, config):
        self.server_url = config.get('server_url')
        if self.server_url is None:
            raise ValueError("The 'server_url' must be provided in the config.")
        self.server_url = self.server_url.strip()

        self.api_key = config.get('api_key')
        if self.api_key is None:
            raise ValueError("The 'api_key' must be provided in the config.")

        self.verify_ssl = config.get('verify_ssl')
        encoded_api_key = base64.b64encode(f'{self.api_key}:X'.encode('utf-8')).decode('utf-8')

        self.headers = {
            'accept': 'application/json',
            'Authorization': f'Basic {encoded_api_key}',
            'Content-Type': 'application/json'
        }

        if not self.server_url.startswith('https://'):
            self.server_url = f'https://{self.server_url}'

    def make_api_call(self, method='GET', endpoint=None, files=None, data=None):
        if endpoint:
            url = f'{self.server_url}{endpoint}'
        else:
            url = f'{self.server_url}'

        headers = self.headers

        logger.debug(f'API Request URL: {url}')
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                files=files,
                data=data,
                verify=self.verify_ssl
            )
            logger.debug(f'API Status Code: {response.status_code}')

            if response.status_code in [200, 201, 204]:
                return response

            error_msg = ERROR_MSGS.get(response.status_code, 'Unknown Error')
            logger.error(f'Failed to request API {url} response is: {response.content} with reason: {response.reason}')
            raise ConnectorError(f'{error_msg}: {response.text}')

        except requests.exceptions.SSLError as e:
            logger.error(f'SSL Error: {e}')
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectionError as e:
            logger.error(f'Connection Error: {e}')
            raise ConnectorError('The request timed out while trying to connect to the remote server')
        except Exception as e:
            logger.error(f'General Error: {e}')
            raise ConnectorError(f'An unexpected error occurred: {e}')


def check_health(config):
    try:
        obj = FreshService(config)
        endpoint = '/api/v2/tickets'
        response = obj.make_api_call(method='GET', endpoint=endpoint)
        logger.info('Returning Project lists response : [{0}]'.format(response))
        if response.status_code in [200, 201]:
            return response.json()
        else:
            raise ConnectorError('Error [{0}] occurred while fetching ticket with status [{1}] code : '.
                                 format(response.text, response.status_code))
    except Exception as err:
        raise ConnectorError(err)


def _get_file_data(iri_type, iri):
    try:
        file_name = None
        if iri_type == 'Attachment ID':
            if not iri.startswith('/api/3/attachments/'):
                iri = '/api/3/attachments/{0}'.format(iri)
            attachment_data = make_request(iri, 'GET')
            file_iri = attachment_data['file']['@id']
            file_name = attachment_data['file']['filename']
        else:
            file_iri = iri
        file_download_response = download_file_from_cyops(file_iri)
        if not file_name:
                file_name = file_download_response['filename']
        file_path = join('/tmp', file_download_response['cyops_file_path'])
        logger.info('file id = %s, file_name = %s' % (file_iri, file_name))
        return file_name, file_path
    except Exception as err:
        logger.exception(str(err))
        raise ConnectorError('could not find attachment with id {}'.format(str(iri)))


def create_ticket(config, params, **kwargs):
    try:
        obj = FreshService(config)
        payload = {}
        subject = params.pop('subject', None)
        description = params.pop('description', None)
        email = params.pop('email', None)
        status = params.pop('status', None)
        priorities = params.pop('priorities', None)
        cc_emails = params.pop('cc_emails', '')
        if subject:
            payload['subject'] = subject

        if description:
            payload['description'] = description

        if email:
            payload['email'] = email

        if status:
            payload['status'] = STATUS_MAP.get(status, 2)  # Default to Open if status is not recognized

        if priorities:
            payload['priority'] = PRIORITY_MAP.get(priorities, 2)  # Default to Medium if priority is not recognized

        if cc_emails:
            payload['cc_emails'] = cc_emails.split(',')

        return obj.make_api_call(method='POST', endpoint='/api/v2/tickets', data=json.dumps(payload)).json()
    except Exception as e:
        logger.exception('{}'.format(e))
        raise ConnectorError('{}'.format(e))


def update_ticket(config, params, **kwargs):
    obj = FreshService(config)
    payload = {}
    ticket_id = params.get('ticket_id')
    subject = params.pop('subject', None)
    description = params.pop('description', None)
    email = params.pop('email', None)
    status = params.pop('status', None)
    priorities = params.pop('priorities', None)
    iri_type = params.get('path')
    iri = params.get('value')

    try:
        if subject:
            payload['subject'] = subject

        if description:
            payload['description'] = description

        if email:
            payload['email'] = email

        if status:
            payload["status"] = STATUS_MAP.get(status)

        if priorities:
            payload['priority'] = PRIORITY_MAP.get(priorities)

        if iri_type and iri:
            file_name, file_path = _get_file_data(iri_type, iri)
            if file_path:
                files = {'attachments[]': (file_name, open(file_path, 'rb'), 'application/octet-stream')}
                data = payload
            else:
                files = None
                data = json.dumps(payload)
        else:

            files = None
            data = json.dumps(payload)
        endpoint = '/api/v2/tickets/{0}'.format(ticket_id)
        response = obj.make_api_call(method='PUT', endpoint=endpoint, data=data, files=files)
        response_json = response.json()
        return response_json

    except Exception as e:
        logger.error('Error in submitFile(): %s' % e)
        logger.exception('Error in submitFile(): %s' % e)
        raise ConnectorError('Error in submitFile(): %s' % e)


def get_ticket_by_id(config, params):
    try:
        obj = FreshService(config)
        response = obj.make_api_call(method='GET', endpoint='/api/v2/tickets/{0}'.format(params.get('ticket_id')))
        response_json = response.json()
        return response_json
    except Exception as e:
        logger.exception('{}'.format(e))
        raise ConnectorError('{}'.format(e))


def delete_ticket_by_id(config, params):
    try:
        obj = FreshService(config)
        ticket_id =params.get('ticket_id')
        response = obj.make_api_call(method='DELETE',
                                 endpoint='/api/v2/tickets/{0}'.format(ticket_id))

        return {'Tcket ID' :ticket_id , 'Status': 'Success'}
    except Exception as e:
        logger.exception('{}'.format(e))
        raise ConnectorError('{}'.format(e))


def filter_tickets_by_query(config, params):
    try:
        obj = FreshService(config)
        query = params.get('query', '')
        encoded_query = urllib.parse.quote(query)
        endpoint = f'/api/v2/tickets/filter?query="{encoded_query}"'
        response = obj.make_api_call(method='GET',
                                 endpoint='/api/v2/tickets/filter?query="{0}"'.format(query))
        response_json = response.json()
        return response_json
    except Exception as e:
        logger.exception('{}'.format(e))
        raise ConnectorError('{}'.format(e))

operations = {
  'create_ticket': create_ticket,
  'update_ticket': update_ticket,
  'get_ticket_by_id': get_ticket_by_id,
  'delete_ticket_by_id': delete_ticket_by_id,
  'filter_tickets_by_query': filter_tickets_by_query
}


