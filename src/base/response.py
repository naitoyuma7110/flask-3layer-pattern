
from flask import Response, jsonify, make_response

def success_response(content: dict={}, header: dict = {}) -> Response:
    return create_success_response(content, header, 200)

def create_success_response(content: dict | None = None, header: dict | None = None,status_code:int = 200)-> Response:
    
    content_json = "" if content is None else jsonify(content)
    response = make_response(content_json, status_code)
    response.headers["Content-Type"] = "application/json"
    response.headers.extend(**header)
    set_additional_header(response)
    
    return response

def set_additional_header(response:Response) -> None:
    response.headers['Content-Language'] = 'ja'