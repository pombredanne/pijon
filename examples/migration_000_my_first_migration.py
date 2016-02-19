import logging


log = logging.getLogger(__name__)


def migrate(input_data):
    """
    You can manipulate your input_data dict freely
    """
    log.debug('migrating {}'.format(input_data))
    input_data['migration'] = 'ok'
    return input_data
