from functools import wraps
from flask import g, request
from base.database import get_session
from base.exception import (InvalidContentTypeError)
from config import Config

def api_filter(content_type: str = 'application/json'):
    
    def _api_filter(func):
        @wraps(func)
        def decorated_function(*args,**kwargs):
            
            if not request.headers.get('Content-Type') == content_type:
                raise InvalidContentTypeError()
            
            try:
                get_session()
                
                res = func(*args, **kwargs)
                
                if _is_updatable(request.method):
                    get_session().commit()

                return res
            
            except Exception as e:
                if _is_updatable(request.method):
                    get_session().rollback()
                raise e
            finally:
                get_session().close()
        
        return decorated_function
    return _api_filter

def _is_updatable(method):
    
    mth = method.upper()
    return mth in ['POST', 'PUT', 'DELETE']
