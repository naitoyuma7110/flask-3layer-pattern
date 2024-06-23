import logging
from flask import request

logger = logging.getLogger('api')

def before_request():
    
    
    path = request.full_path
    if path != '/?': # ルートパス
        method = request.method
        remote_addr = _get_remote_addr()
        # stat = str(request._status_code)
        stat = str(request)
        body = str(request.get_json(silent=True))
        logger.info(f'[API end] {method} : {path} : {stat} - {remote_addr}')
        logger.debug(f'[req] {body}')

def after_request(response):
    
    path = request.full_path
    if path != '/?':
        method = request.method
        remote_addr = _get_remote_addr()
        stat = str(request)
        body = str(request.get_json(silent=True))
        logger.info(f'[API end] {method} : {path} : {stat} - {remote_addr}')
        logger.debug(f'[req] {body}')
        
    return response

def _get_remote_addr():
    return request.remote_addr if request.remote_addr is not None else 'unknown-From'