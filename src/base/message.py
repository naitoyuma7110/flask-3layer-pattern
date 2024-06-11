from flask import current_app

def get_error_message(err_type: str, invalid_msgs: dict | None = None) -> dict:
    res_msg = _make_error_res(err_type)
    
    if invalid_msgs is not None:
        res_msg['invalid_params'] = invalid_msgs
    
    return res_msg

def _make_error_res(err_type: str) -> dict:
    
    locale = 'ja'
    res_msg = current_app.config['ERROR_RESPONSE'][locale][err_type]
    
    return{
        'type':err_type,
        'title':res_msg['title'],
        'status':res_msg['status']
    }
    # return {
    #     'type':err_type,
    #     'title':'指定されたURLは存在しません',
    #     'status':404,
    # }