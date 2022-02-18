_RED = '\033[22;31m'
_GREEN = '\033[22;32m'
_YELLOW = '\033[22;33m'
_MAGENTA = '\033[22;35m'
_CYAN = '\033[22;36m'
_BLUE = '\033[22;34m'
_BLUE = '\033[0;34m'
_DEFAULT = '\033[0;22m'
_RESET = '\033[0;22m'


class terminal_color_util:
    RED = _RED
    GREEN = _GREEN
    YELLOW = _YELLOW
    MAGENTA = _MAGENTA
    CYAN = _CYAN
    BLUE = _BLUE
    DEFAULT = _DEFAULT
    RESET = _RESET

    FUNCTION = _CYAN
    FILE = _GREEN
    DIRECTORY = _BLUE
    VARIABLE = _MAGENTA
    VALUE = _GREEN
    ERROR = _RED
    WARNING = _YELLOW

    @staticmethod
    def disable():
        terminal_color_util.DEFAULT = ''
        terminal_color_util.FUNCTION = ''
        terminal_color_util.FILE = ''
        terminal_color_util.DIRECTORY = ''
        terminal_color_util.VARIABLE = ''
        terminal_color_util.VALUE = ''
        terminal_color_util.ERROR = ''
        terminal_color_util.WARNING = ''

    @staticmethod
    def enable():
        terminal_color_util.init()
