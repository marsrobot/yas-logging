import os
import sys
import logging
import threading

from .Logger import Logger

dummy_logger_name = dict()

_loggers = dict()

global_props = dict()


class LoggingContextFilter(logging.Filter):
    def filter(self, record):
        record.ThreadId = threading.get_ident()
        for k in global_props.keys():
            setattr(record, k, global_props[k])
        return True


class log_util_impl:
    @staticmethod
    def get_logger(logger_name: str = None, logging_level=logging.INFO):
        global _loggers
        global dummy_logger_name

        if logger_name is None or logger_name == '':
            if dummy_logger_name == {}:
                dummy_logger_name = 'YAS_LOGGER'
            logger_name = dummy_logger_name

        if logger_name not in _loggers:
            logger = Logger(logger_name, logging_level=logging_level)
            logger.addFilter(LoggingContextFilter())
            _loggers[logger_name] = logger

        return _loggers[logger_name]

    @staticmethod
    def set_global_properties(props):
        global global_props
        global_props = props


get_logger = log_util_impl.get_logger
set_global_properties = log_util_impl.set_global_properties

from .LoggingConsoleFormatter import LoggingConsoleFormatter
from .LoggingFileFormatter import LoggingFileFormatter
