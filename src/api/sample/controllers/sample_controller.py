from flask import Blueprint, jsonify
from injector import inject
from api.sample.services.sample_service import ISampleService
from base.utils import dataclass_util
from base.response import success_response

api = Blueprint('sample_controller', __name__)
"""
'sample_controller' : Blueprint名
__name__ : このファイルのディレクトリ名
"""

@api.route('/hello', methods=['GET'])
def hello():
    return 'hello'


@api.route('/get_sample/<string:text>', methods=['GET'])
@inject
def get_sample(text: str, sample_service:ISampleService):
    
    result = sample_service.get_sample(text)
    
    return success_response(dataclass_util.todict(result))