import os
from tests.basetest import BaseTest

class BaseTestController(BaseTest):
    '''
    共通テストケース基底クラス
    '''
    
    def ctx_path(self) -> str:
        return os.getenv('SAMPLE_API_PATH')
        
        
    def headers(self, key: str = None) -> dict:
        '''
        ヘッダ情報を取得
        '''
        
        return {'content-type':'application/json'}
    
    def make_header_with_token(self) -> dict:
        headers: dict = self.headers()
        
        return headers