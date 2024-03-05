"""
Copyright start
MIT License
Copyright (c) 2023 Fortinet Inc
Copyright end
"""

from connectors.core.connector import Connector, get_logger, ConnectorError
from .operations import check_health, operations
logger = get_logger('fresh-service-desk-msp')


class FreshService(Connector):

    def execute(self, config, operation, params, **kwargs):
        try:
            operation = operations.get(operation)
            return operation(config, params, **kwargs)
        except Exception as err:
            logger.error(str(err))
            raise ConnectorError(str(err))

    def check_health(self, config):
        return check_health(config)
