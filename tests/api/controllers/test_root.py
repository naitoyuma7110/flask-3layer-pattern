from tests.api.controllers.basetest_controller import BaseTestController

class TestRoot(BaseTestController):
    
    def test_root(self, client):
        
        res = client.get('/')
        assert res.status_code == 200
        
        res = client.get(self.ctx_path() + '/')
        assert res.status_code == 200
        
    def test_root_notfound(self, client):
        
        res = client.get('/xxx/')
        json_data = res.get_json()
        assert res.status_code == 404
        assert json_data['title'] == '指定されたURLは存在しません'
        assert json_data['type'] == 'uri-not-found'