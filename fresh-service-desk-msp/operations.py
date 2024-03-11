"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import requests
import json
import base64
from os.path import join
from connectors.core.connector import get_logger, ConnectorError
from integrations.crudhub import make_request
from connectors.cyops_utilities.builtins import download_file_from_cyops
logger = get_logger('fresh-service-desk-msp')


def get_config(config):
    try:
        if config is not None:
            server_url = config.get('server')
            username = config.get('username')
            password = config.get('password')
            verify_ssl = config.get('verify_ssl')
            return server_url, username, password, verify_ssl
    except Exception as Err:
        logger.warn('Error occured while extracting conf :[{0}] '.format(Err))
        raise ConnectorError(Err)


def generate_basic_auth_header(username, password):
    credentials = f"{username}:{password}"
    credentials_b64 = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return f"Basic {credentials_b64}"


def check_health(config):
    try:
        endpoint = '/api/v2/tickets'
        response = make_api_call(config, method='GET', endpoint=endpoint)
        logger.info('Returning Project lists response : [{0}]'.format(response))
        if response.status_code in [200, 201]:
            return response.json()
        else:
            raise ConnectorError('Error [{0}] occurred while fetching jira ticket status with status [{1}] code : '.
                                 format(response.reason, response.status_code))
    except Exception as err:
        raise ConnectorError(err)


def get_file_data(iri_type, iri, **kwargs):
    try:
        file_name = None
        if iri_type == 'Attachment ID':
            if not iri.startswith('/api/3/attachments/'):
                iri = '/api/3/attachments/{0}'.format(iri)
            attachment_data = make_request(iri, 'GET')
            file_iri = attachment_data['file']['@id']
            file_name = attachment_data['file']['filename']
        if iri_type == 'File IRI':
            if not iri.startswith('/api/3/files/'):
                iri = '/api/3/files/{0}'.format(iri)
                file_iri = iri
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


def make_api_call(config, method='GET', endpoint=None, files=None, data=None):
    server, username, password, verify_ssl = get_config(config)
    if server.startswith('https://'):
        server = server.strip('/')
    else:
        server = 'https://{0}'.format(server)
    if files:
        headers = None
    else:
        headers = {'content-type': 'application/json', 'accept': 'application/json'}
    if endpoint:
        url = '{0}{1}'.format(server, endpoint)
    else:
        url = server
        return url
    logger.info('Request URL {}'.format(url))
    try:
        response = requests.request(url=url, method=method, auth=(username, password), headers=headers, files=files,
                                    data=data, verify=verify_ssl)
        if response.status_code in [200, 201, 204]:
            return response
        elif response.status_code == 401:
            logger.info('Unauthorized: Invalid credentials')
            raise ConnectorError('Unauthorized: Invalid credentials')
        else:
            logger.info(
                'Failed to request API {0} response is : {1} with reason: {2}'.format(str(url), str(response.content),
                                                                                      str(response.reason)))
            raise ConnectorError(
                'Failed to request API {0} response is :{1} with reason: {2}'.format(str(url), str(response.content),
                                                                                     str(response.reason)))
    except requests.exceptions.SSLError as e:
        logger.exception('{}'.format(e))
        raise ConnectorError('{}'.format('SSL certificate validation failed'))
    except requests.exceptions.ConnectionError as e:
        logger.exception('{}'.format(e))
        raise ConnectorError('{}'.format('The request timed out while trying to connect to the remote server'))
    except Exception as e:
        logger.exception('{}'.format(e))
        raise ConnectorError('{}'.format(e))


def create_ticket(config, params, **kwargs):
    try:
        payload = {}
        subject = params.pop('subject', None)
        description = params.pop('description', None)
        email = params.pop('email', None)
        status = params.pop('status', None)
        priorities = params.pop('priorities', None)
        cc_emails = params.pop('cc_emails', None)
        if subject:
            payload['subject'] = subject

        if description:
            payload['description'] = description

        if email:
            payload['email'] = email

        if status:
            status_map = {'Open': 2, 'Pending': 3, 'Resolved': 4, 'Closed': 5}
            payload['status'] = status_map.get(status, 2)  # Default to Open if status is not recognized

        if priorities:
            priority_map = {'Low': 1, 'Medium': 2, 'High': 3, 'Urgent': 4}
            payload['priority'] = priority_map.get(priorities, 2)  # Default to Medium if priority is not recognized

        if cc_emails:
            payload['cc_emails'] = cc_emails.split(',')

        return make_api_call(config, method='POST', endpoint='/api/v2/tickets', data=json.dumps(payload)).json()
    except Exception as e:
        logger.exception('{}'.format(e))
        raise ConnectorError('{}'.format(e))


def get_ticket_by_id(config, params, **kwargs):
    try:
        response = make_api_call(config, method='GET', endpoint='/api/v2/tickets/{0}'.format(params.get('ticket_id')))
        response_json = response.json()
        return response_json
    except Exception as e:
        logger.exception('{}'.format(e))
        raise ConnectorError('{}'.format(e))

def delete_ticket_by_id(config, params, **kwargs):
    try:
        response = make_api_call(config, method='DELETE', endpoint='/api/v2/tickets/{0}'.format(params.get('ticket_id')))
        response_json = response.json()
        return response_json
    except Exception as e:
        logger.exception('{}'.format(e))
        raise ConnectorError('{}'.format(e))


def filter_tickets_by_query(config, params, **kwargs):
    try:
        response = make_api_call(config, method='GET', endpoint='/api/v2/search/tickets?query="{0}"'.format(params.get('query')))
        response_json = response.json()
        return response_json
    except Exception as e:
        logger.exception('{}'.format(e))
        raise ConnectorError('{}'.format(e))


def update_ticket(config, params, **kwargs):

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
            status_map = {'Open': 2, 'Pending': 3, 'Resolved': 4, 'Closed': 5}
            payload["status"] = status_map.get(status)

        if priorities:
            priority_map = {'Low': 1, 'Medium': 2, 'High': 3, 'Urgent': 4}
            payload['priority'] = priority_map.get(priorities)

        if iri_type and iri:
            file_name, file_path = get_file_data(iri_type, iri)
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
        response = make_api_call(config, method='PUT', endpoint=endpoint, data=data, files=files)
        response_json = response.json()
        return response_json

    except Exception as e:
        logger.error('Error in submitFile(): %s' % e)
        logger.exception('Error in submitFile(): %s' % e)
        raise ConnectorError('Error in submitFile(): %s' % e)


operations = {
    'create_ticket': create_ticket,
    'get_ticket_by_id': get_ticket_by_id,
    'update_ticket': update_ticket,
    'delete_ticket_by_id': delete_ticket_by_id,
    'filter_tickets_by_query': filter_tickets_by_query
}