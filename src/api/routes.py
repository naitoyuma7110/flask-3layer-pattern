from flask import Flask, jsonify 

def init_routes(app:Flask)-> None:
    
    from base.response import success_response
    
    sample_ctx_path = app.config['SAMPLE_API_PATH']
    
    @app.route('/', methods=['GET'])
    def get_root():
        return success_response(content=None)
    
    @app.route(sample_ctx_path + '/', methods=['GET'])
    def get_ctx_root():
        return success_response(content=None)
    
    from api.sample.controllers import sample_controller
    
    
    sample_path = sample_ctx_path + '/v1'
    
    app.register_blueprint(sample_controller.api, url_prefix=sample_path)