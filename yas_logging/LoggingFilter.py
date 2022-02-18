import socket
from logging import Filter


class LoggingFilter(Filter):
    hostname = socket.gethostname()

    def filter(record):
        record.hostname = LoggingFilter.hostname
        return True
