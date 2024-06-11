
from flask import Response, jsonify, make_response
from base.exception import (ResponseError, InvalidParametersError, UriNotFoundError)
from base import message

def success_response(content: dict={}, header: dict = {}) -> Response:
    return _create_success_response(content, header, 200)

def response_error(error: ResponseError) -> Response:
    return _create_error_response(error.error_type)
    
def response_error_params(error: InvalidParametersError) -> Response:
    return _create_error_response(error.error_type, error.invalid_msgs)

def response_error_notfound(ex: Exception) -> Response:
    error = UriNotFoundError()
    return _create_error_response(error.error_type)
    


def _create_success_response(content: dict | None = None, header: dict | None = None,status_code:int = 200)-> Response:
    
    content_json = "" if content is None else jsonify(content)
    response = make_response(content_json, status_code)
    response.headers["Content-Type"] = "application/json"
    response.headers.extend(**header)
    _set_additional_header(response)
    
    return response

def _create_error_response(error_type: str, invalid_params: dict | None = None) -> Response:
    content = message.get_error_message(error_type, invalid_params)
    status = content['status']
    response = make_response(jsonify(content), status)
    response.headers["Content-Type"] = "application/json"
    response.headers["Access-Control-Allow-Origin"] = "*"
    _set_additional_header(response)
    
    # TODO:set loggera
    
    return response
    

def _set_additional_header(response:Response) -> None:
    response.headers['Content-Language'] = 'ja'
    
