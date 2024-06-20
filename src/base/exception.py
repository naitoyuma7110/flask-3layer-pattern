import message_config as msg 

class InvalidContentTypeError(Exception):
    
    error_type = msg.ERR_TYPE_INVALID_CTYPE
    

class ResponseError(Exception):
    
    def __init__(self, error_type: str | None = None):
        
        Exception.__init__(self)
        if error_type is not None:
            self.error_type = error_type

class InvalidParametersError(ResponseError):
    
    error_type = msg.ERR_TYPE_INVALID_PARAM
    
    def __init__(self, invalid_msgs:dict = {}):
        
        ResponseError.__init__(self)
        self.invalid_msgs = invalid_msgs
        
class UriNotFoundError(ResponseError):
    error_type = msg.ERR_TYPE_URI_NOTFOUND
