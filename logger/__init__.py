import logging
import logging.config

from config import settings

logging.config.dictConfig(settings.logging)
logging.debug('root logger configured')


def custom_logger(name: str):
    return logging.getLogger(name)
