from environs import Env
from erppeek import Client
from pool_transport import PoolTransport

test_env = Env()
test_env.read_env('tests/.env.test')

HTTP_CONF = test_env.json('HTTP_CONF')
HTTPS_CONF = test_env.json('HTTPS_CONF')


class TestPoolTransport:

    def test_http_connection(self):
        erp_client = Client(transport=PoolTransport(), **HTTP_CONF)
        assert erp_client is not None

    def test_https_connection(self):
        erp_client = Client(transport=PoolTransport(secure=True), **HTTPS_CONF)
        assert erp_client is not None

    def test_call_rpcmethod(self):
        erp_client = Client(transport=PoolTransport(), **HTTP_CONF)
        model = erp_client.model('account.account')

        assert model._name == 'account.account'
