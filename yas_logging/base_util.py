import os
import sys
import getpass
import socket
from typing import Union

DNS_IP = None


class base_util:
    @staticmethod
    def get_hostname(address: str = None) -> Union[str, None]:
        """
        unreliable to check whether IP is alive. For some alive hosts, this function
        return "[Errno 1] Unknown host".
        """

        try:
            host = socket.gethostname()
            return host
        except BaseException as ex:
            try:
                hostname = socket.gethostbyaddr(address)
                return hostname[0]
            except BaseException as ex:
                return None

        return None

    @staticmethod
    def set_dns_ip(ip):
        global DNS_IP
        DNS_IP = ip

    @staticmethod
    def get_ip():
        global DNS_IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect((DNS_IP, 1))
            ip = s.getsockname()[0]
        except BaseException as ex:
            print(ex)
            ip = None
        finally:
            s.close()
        return ip

    @staticmethod
    def get_user():
        try:
            return getpass.getuser()
        except BaseException as ex:
            return None

    @staticmethod
    def is_docker():
        return os.path.exists('/.dockerenv')
