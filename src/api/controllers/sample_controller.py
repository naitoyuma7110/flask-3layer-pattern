from flask import Blueprint, jsonify
from injector import inject
from api.services.sample_service import ISampleService

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
    
    return jsonify(result)