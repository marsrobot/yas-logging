from .base_util import base_util


class LoggingTemplate:
    @staticmethod
    def logging_template():
        host = base_util.get_hostname()
        user = base_util.get_user()
        host_info = '{}:{} '.format(host, user)
        fmt_template = '%(asctime)s %(msecs)dms ' \
                       + host_info \
                       + '{}' \
                       + '[%(name)s:*%(levelname)s*] ' \
                       + '%(msg)s' \
                       + '{}' \
                       + ' %(pathname)s:%(lineno)d %(process)d:%(thread)d'
        return fmt_template
