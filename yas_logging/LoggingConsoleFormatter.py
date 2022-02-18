import logging
import logging.config

from .LoggingTemplate import LoggingTemplate
from .terminal_color_util import terminal_color_util


class LoggingConsoleFormatter(logging.Formatter):

    def __init__(self):
        super().__init__(fmt='%(levelno)d: %(msg)s', datefmt="%Y-%m-%dT%H:%M:%S%z", style='%')
        fmt_template = LoggingTemplate.logging_template()
        self.debug_format = fmt_template.format(terminal_color_util.DEFAULT, terminal_color_util.RESET)
        self.info_format = fmt_template.format(terminal_color_util.GREEN, terminal_color_util.RESET)
        self.warn_format = fmt_template.format(terminal_color_util.YELLOW, terminal_color_util.RESET)
        self.error_format = fmt_template.format(terminal_color_util.RED, terminal_color_util.RESET)
        self.other_format = fmt_template.format(terminal_color_util.DEFAULT, terminal_color_util.RESET)

    def format(self, record):
        format_orig = self._style._fmt
        if record.levelno == logging.DEBUG:
            self._style._fmt = self.debug_format
        elif record.levelno == logging.INFO:
            self._style._fmt = self.info_format
        elif record.levelno == logging.WARN:
            self._style._fmt = self.warn_format
        elif record.levelno == logging.ERROR:
            self._style._fmt = self.error_format
        else:
            self._style._fmt = self.other_format

        result = logging.Formatter.format(self, record)

        self._style._fmt = format_orig
        return result
