import os
import sys
import logging
from logging.handlers import RotatingFileHandler

from yas_logging import LoggingConsoleFormatter
from yas_logging import LoggingFileFormatter
from yas_logging import get_logger
from yas_logging import set_global_properties

if __name__ == '__main__':
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setFormatter(LoggingConsoleFormatter())

    log_file_path = '/tmp/test.log'
    file_handler = RotatingFileHandler(log_file_path, maxBytes=(1048576 * 1024), backupCount=7)
    file_handler.setFormatter(LoggingFileFormatter())

    logger_name = 'YasDemoLogger'
    logging_level = logging.DEBUG
    logger = get_logger(logger_name, logging_level)
    props = {
        'Department': 'Sales',
        'Location': 'NYC',
        'Environment': 'PRODUCTION',
    }
    set_global_properties(props)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.debug('Hello World debug')
    logger.info('Hello World info')
    try:
        1 / 0
    except Exception as ex:
        logger.error('Hello World error', exception=ex)
