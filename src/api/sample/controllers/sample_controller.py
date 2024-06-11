from flask import Blueprint, request
from injector import inject
from api.sample.services.sample_service import ISampleService
from base.utils import dataclass_util
from base.exception import InvalidParametersError
from base.response import success_response

api = Blueprint('sample_controller', __name__)
"""
'sample_controller' : Blueprint名
__name__ : このファイルのディレクトリ名
"""

@api.route('/sample/<string:text>', methods=['GET'])
@inject
def get_sample(text: str, sample_service:ISampleService):
    
    
    result = sample_service.get_sample(text)
    
    return success_response(dataclass_util.todict(result))

# @api.route('/sample', methods=['POST'])
# @inject
# def get_sample(text: str, sample_service:ISampleService):

#     try:
#         req_json = {} if request.json is None else request.json
#     except Exception:
#         raise InvalidParametersError()
        
#     result = sample_service.get_sample(text)
    
#     return success_response(dataclass_util.todict(result))