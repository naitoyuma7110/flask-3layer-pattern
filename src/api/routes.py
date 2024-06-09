from flask import Flask 

def init_routes(app:Flask)-> None:
    
    @app.route('/', methods=['GET'])
    def root():
        return 'hello'
    
    from api.sample.controllers import sample_controller
    
    sample_api_context = "/sample" 
    
    sample_path = sample_api_context + '/v1'
    
    app.register_blueprint(sample_controller.api, url_prefix=sample_path)