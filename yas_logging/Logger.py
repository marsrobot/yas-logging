from .LoggerBase import LoggerBase


class Logger(LoggerBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def build_str(*args, **kwargs):
        s = ''
        for arg in args:
            if isinstance(arg, str):
                s = s + arg
            else:
                s = s + str(arg)
        return s

    def debug(self, *args, **kwargs) -> None:
        super(Logger, self).debug(Logger.build_str(*args, **kwargs))

    def info(self, *args, **kwargs) -> None:
        super(Logger, self).info(Logger.build_str(*args, **kwargs))

    def warn(self, *args, **kwargs) -> None:
        super(Logger, self).warn(Logger.build_str(*args, **kwargs))

    def warning(self, *args, **kwargs) -> None:
        super(Logger, self).warning(Logger.build_str(*args, **kwargs))

    def error(self, *args, **kwargs) -> None:
        super(Logger, self).error(Logger.build_str(*args), **kwargs)
