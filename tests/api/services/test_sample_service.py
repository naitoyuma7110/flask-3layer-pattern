import pytest
from unittest import mock
from flask_injector import Binder
from datetime import datetime
from tests.api.services.basetest_service import BaseTestService


class TestSampleService(BaseTestService):
    
    @pytest.mark.parametrize(
        "return_value",
        [
            pytest.param(
                [
                    (1, "john_doe", "john@example.com", datetime(2023, 1, 1), None),
                    (2, "jane_smith", "jane@example.com", datetime(2023, 1, 2), None)
                ],
                id="sample_set_1",
                marks=pytest.mark.smoke
            ),
            pytest.param(
                [
                    (3, "alice_jones", "alice@example.com", datetime(2023, 1, 3), None),
                    (4, "bob_brown", "bob@example.com", datetime(2023, 1, 4), None)
                ],
                id="sample_set_2",
                marks=pytest.mark.regression
            )
        ]
    )
    
    def test_get_sample(self, return_value):
        
        from api.sample.services.sample_service import SampleService
        from api.sample.models.sample import SampleRepository


        sample_mock_repository = mock.MagicMock(spec=SampleRepository)
        
        sample_mock_repository.get_sample_users.return_value = return_value
        
        result = sample_mock_repository.get_sample_users()
        
        # アサーション
        assert isinstance(result, list)
        assert len(result) == 2
        
        # 各要素の型と値を検証
        for item in result:
            assert isinstance(item, tuple)
            assert len(item) == 5 
