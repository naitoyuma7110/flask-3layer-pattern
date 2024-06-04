from flask import Blueprint, Response, request

api = Blueprint('sample_controller', __name__)
"""
'sample_controller' : Blueprint名
__name__ : このファイルのディレクトリ名
"""

@api.route('/get_sample', methods=['GET'])
def get_sample():
    return 'sample'