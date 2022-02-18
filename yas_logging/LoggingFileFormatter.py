import os
import sys
import logging
import logging.config

from .LoggingTemplate import LoggingTemplate


class LoggingFileFormatter(logging.Formatter):

    def __init__(self):
        fmt_template = LoggingTemplate.logging_template()
        super().__init__(fmt='%(levelno)d: %(msg)s', datefmt="%Y-%m-%dT%H:%M:%S%z", style='%')
        self.fmt = fmt_template.format('', '')

    def format(self, record):
        format_orig = self._style._fmt
        self._style._fmt = self.fmt

        result = logging.Formatter.format(self, record)

        self._style._fmt = format_orig
        return result
