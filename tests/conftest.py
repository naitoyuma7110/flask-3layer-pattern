import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.dirname(os.abspath(__file__)) + "/../src/"))

@pytest.fixture(scope='session')
def app():
    
    from api import create_app
    return create_app(('unittest'))

@pytest.fixture
def client(app):
    
    return app.test_client()