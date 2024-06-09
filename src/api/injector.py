from flask import Flask
from flask_injector import FlaskInjector, Binder, request

def di_config(binder: Binder) -> None:
    
    from api.sample.services.sample_service import (SampleService, ISampleService)
    
    binder.bind(ISampleService, to=SampleService, scope=request)
    
    from api.sample.models.sample import (SampleRepository, ISampleRepository)
    
    binder.bind(ISampleRepository, to=SampleRepository, scope=request)


def init_di(app:Flask):
    FlaskInjector(app=app, modules=[di_config])