from urllib import parse
from xmlrpc.client import Transport as XMLRPCTransport

from urllib3 import HTTPConnectionPool, HTTPSConnectionPool


__all__ =  [
    'PoolTransport'
]


def is_secure(uri):
    uri_parsed = parse.urlparse(uri)

    return bool(uri_parsed.scheme) and uri_parsed.scheme[-1] == 's'


class PoolTransport(XMLRPCTransport):

    def __init__(
        self, use_datetime=False, use_builtin_types=False, *, headers=(),
        **kwds
    ):
        secure = is_secure(kwds.get('server', ''))
        super().__init__(
            use_datetime=use_datetime,
            use_builtin_types=use_builtin_types,
            headers=headers
        )
        self._pool_class = HTTPSConnectionPool if secure else HTTPConnectionPool

    def make_connection(self, host):
        if self._connection and host == self._connection[0]:
            return self._pool._get_conn()

        chost, self._extra_headers , x509 = self.get_host_info(host)
        hostname, port = chost.split(':')

        self._pool = self._pool_class(hostname, port)

        self._connection = host, self._pool
        return self._pool._get_conn()
