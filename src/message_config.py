ERR_TYPE_INVALID_PARAM = 'invalid-parameters'
ERR_TYPE_URI_NOTFOUND = 'uri-not-found'

ERROR_RESPONSE = {
    'ja':{
        ERR_TYPE_INVALID_PARAM:{
                'status':400,
                'title':'リクエストパラメータ不正'
            },
        ERR_TYPE_URI_NOTFOUND:{
                'status':404,
                'title':'指定されたURLは存在しません'
            }
        }
}