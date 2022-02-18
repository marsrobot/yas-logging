import os
import sys
import copy
import collections
import datetime
import time
import atexit
import traceback
import threading
import logging
import logging.config
from logging.handlers import SysLogHandler

from .LoggingFilter import LoggingFilter
from .base_util import base_util
from .debug_util import debug_util

logger_base = None


class LoggerBase(logging.Logger):
    def __init__(self, logger_name: str, logging_level: any = logging.DEBUG):
        super().__init__(name=logger_name)
        self.setLevel(logging_level)
        pass

    def makeRecord(self, name, level, fn, lno, msg, args, exc_info, func=None, extra=None, sinfo=None):
        fn = None
        lno = None
        func = None
        rv = logging.LogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)
        if extra is not None:
            for key in extra:
                if (key in ["message", "asctime"]) or (key in rv.__dict__):
                    # raise KeyError("Attempt to overwrite %r in LogRecord" % key)
                    pass
                rv.__dict__[key] = extra[key]
        rv.__dict__ = dict(collections.OrderedDict(sorted(rv.__dict__.items())))
        return rv

    @staticmethod
    def get_code_location() -> str:
        rv = debug_util.code_location(4)
        return rv

    @staticmethod
    def get_code_location_object() -> str:
        rv = debug_util.code_location_object(4)
        return rv

    @staticmethod
    def use_syslog():
        use_syslog = os.path.isfile('/dev/log')
        return use_syslog

    @staticmethod
    def init_syslog():
        if LoggerBase.use_syslog():
            my_syslog = SysLogHandler(address='/dev/log')
            my_syslog.addFilter(LoggingFilter())
            format = '[%(name)s:*%(levelname)s*] %(msg)s %(process)d:%(thread)d'
            formatter = logging.Formatter(format)
            my_syslog.setFormatter(formatter)
            return my_syslog
        return None

    @staticmethod
    def shutdown_logging():
        logging.shutdown()
        time.sleep(0.01)

    @staticmethod
    def dict_merge(dict1: dict, dict2: dict) -> dict:
        d3 = copy.deepcopy(dict2)
        for k in dict1:
            d3[k] = dict1[k]
        return d3

    @staticmethod
    def get_info():
        user = base_util.get_user()
        thread_id = threading.get_ident()

        # import psutil
        # proc = psutil.Process()
        # open_files = len(proc.open_files())
        res = dict()

        res = LoggerBase.dict_merge(res, {
            # 'open_files': open_files,
            'thread_id': thread_id,
            'time': datetime.datetime.now().isoformat(),
            'user': user,
        })
        filtered_res = dict()
        for k in res:
            v = res[k]
            if v is not None and v != '':
                filtered_res[k] = v
        return filtered_res

    def debug(self, obj: any) -> None:
        loc = LoggerBase.get_code_location_object()
        stack_trace = traceback.format_stack()[:-1]
        stack_info = ''.join(stack_trace)

        extra = LoggerBase.dict_merge(LoggerBase.get_info(), {
            # 'file': loc['filename'],
            'function': loc['function'],
            'lineno': loc['lineno'],
            'pathname': loc['filename'],
            'stack_trace': stack_info,
        })
        super().debug(str(obj), extra=extra)
        return

    def info(self, obj: any) -> None:
        loc = LoggerBase.get_code_location_object()
        stack_trace = traceback.format_stack()[:-1]
        stack_info = ''.join(stack_trace)
        extra = LoggerBase.dict_merge(LoggerBase.get_info(), {
            'function': loc['function'],
            'lineno': loc['lineno'],
            'pathname': loc['filename'],
            'stack_trace': stack_info,
        })
        super().info(obj, extra=extra)
        return

    def warn(self, obj: str) -> None:
        loc = LoggerBase.get_code_location_object()
        stack_trace = traceback.format_stack()[:-1]
        stack_info = ''.join(stack_trace)
        extra = LoggerBase.dict_merge(LoggerBase.get_info(), {
            # 'file': loc['filename'],
            'function': loc['function'],
            'lineno': loc['lineno'],
            'pathname': loc['filename'],
            'stack_trace': stack_info,
        })
        super().warning(str(obj), extra=extra)
        return

    def warning(self, obj: str) -> None:
        loc = LoggerBase.get_code_location_object()
        stack_trace = traceback.format_stack()[:-1]
        stack_info = ''.join(stack_trace)
        extra = LoggerBase.dict_merge(LoggerBase.get_info(), {
            # 'file': loc['filename'],
            'function': loc['function'],
            'lineno': loc['lineno'],
            'pathname': loc['filename'],
            'stack_trace': stack_info,
        })
        super().warning(str(obj), extra=extra)
        return

    def error(self, obj: str, exception: BaseException = None) -> None:
        loc = LoggerBase.get_code_location_object()
        stack_trace = traceback.format_stack()[:-1]
        stack_info = ''.join(stack_trace)
        extra = LoggerBase.dict_merge(LoggerBase.get_info(), {
            # 'file': loc['filename'],
            'error': exception,
            'function': loc['function'],
            'lineno': loc['lineno'],
            'pathname': loc['filename'],
            'stack_trace': stack_info,
            'traceback': traceback.format_exc(),
        })
        super().error(str(obj) + ': ' + str(exception), extra=extra)

    def setLevel(self, level) -> None:
        super().setLevel(level)

    def log(self, x_str, value):
        print('{}={}'.format(x_str, value))

    def __del__(self):
        # LoggerBase.shutdown_logging()
        pass

    @staticmethod
    def get_logger_base():
        global logger_base
        if logger_base is None:
            logger_base = LoggerBase('MARS')
        return logger_base

# atexit.register(LoggerBase.shutdown_logging)
