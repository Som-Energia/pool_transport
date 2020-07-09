# Pool Transport

Pool transport class enable make concurrent requests to the same xmlrpc server.
:warning: **alpha release!!** don't use it in production environments!! **posible API changes**

# Installation

```bash
pip install git+https://github.com/Som-Energia/pool_transport.git
```

# Use
## In erppeek connections
Here an example of how to use PoolTransport

```python
from erppeek import Client
from pool_transport import PoolTransport

HTTP_CONF={"server":"http://localhost:80", "db":"database", "user":"foo", "password":"pass"}

erp_client = Client(transport=PoolTransport(), **HTTP_CONF)
```

For secure connections:
```python
HTTPS_CONF={"server":"https://localhost:443", "db":"database", "user":"foo", "password":"pass"}
erp_client = Client(transport=PoolTransport(secure=True), **HTTPS_CONF)
```

# Contribute

1. Fork the repository on GitHub.
2. Set up your development setup
```bash
$> pip install -e .
$> pipenv install --dev
```
3. Run the tests to confirm they all pass on your system.
3.1. Copy `env.test.example` to `env.test` and adapt it with the information of your xmlrpc server
```bash
$> cp tests/env.test.example tests/env.test
$> pytest
```
4. Make your change and run the entire test suite again and confirm that all tests pass including the ones you just added.
5. Create us a GitHub Pull Request to the main repository’s master branch. GitHub Pull Requests are the expected method of code collaboration on this project.

# Changes

## v0.0.1-alpha
* PoolTransport class creation

# License
This project uses the following license: [GNU AFFERO GENERAL PUBLIC LICENSE](LICENSE). 
