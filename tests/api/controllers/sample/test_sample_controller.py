import json
from unittest import mock
import pytest
from flask_injector import Binder
from tests.api.controllers.basetest_controller import BaseTestController
from api.sample.services.sample_service import Samples, Sample
from dataclasses import dataclass, asdict

class TestSampleController(BaseTestController):
    
    def make_header(self):
        headers: dict = self.make_header_with_token()
        
        return headers
    
    def create_client(self, app) -> None:
    
        def mockset(binder: Binder) -> None:
            
            from api.sample.services.sample_service import (ISampleService, SampleService)
            
            self.mock_sample_service = mock.MagicMock(spec=SampleService)
            self.mock_sample_service.get_sample.return_value = None
            
            binder.bind(ISampleService, to=self.mock_sample_service)
            
        return self.make_client(app, mockset)
    
    def test_sample(self, app):
        
        client = self.create_client(app)
        
        headers:dict = self.make_header()
        
        # モックデータの設定
        mock_samples = Samples(
                samples=[
                    Sample(sample="hello", username="john_doe", email="john@example.com"),
                    Sample(sample="hello", username="jane_smith", email="jane@example.com")
                ]
            )

        self.mock_sample_service.get_sample.return_value = mock_samples

        url = '/v1/sample/sample'
        res = client.get(self.ctx_path() + url, headers=headers)

        assert res.status_code == 200

        # レスポンスのJSONデータを取得
        json_data = res.get_json()

        # レスポンスが期待されるJSONデータと一致するかを確認
        expected_data = {
            'samples': [
                asdict(sample) for sample in mock_samples.samples
            ]
        }
        assert json_data == expected_data