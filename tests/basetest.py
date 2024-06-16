from typing import Callable
from flask.testing import FlaskClient
from flask_injector import FlaskInjector

class BaseTest():
    
    def get_client(self, app)-> FlaskClient:
        
        return app.test_client()
    
    def make_client(self, app, mock_bind: Callable) -> FlaskClient:
        if mock_bind is not None:
            FlaskInjector(app=app, modules=[mock_bind])
        return app.test_client()