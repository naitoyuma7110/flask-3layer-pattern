import pytest
from tests.api.models.basetest_repository import BaseTestRepository
from datetime import datetime
from sqlalchemy.orm.query import Row
from sqlalchemy.sql import text

class TestSampleRepository(BaseTestRepository):
    
    delete_text: str = \
        '''
        DELETE FROM users;
        '''
        
    insert_users_text: str = \
        '''
        INSERT INTO public.users(
            id,
            username,
            email,
            created_at,
            deleted_at)
            VALUES
                (DEFAULT, 'john_doe', 'john@example.com', NOW(), NULL),
                (DEFAULT, 'jane_smith', 'jane@example.com', NOW(), NULL);
        '''
        
    def test_get_sample_users(self, session):
        
        session.execute(text(self.delete_text))
        
        session.execute(text(self.insert_users_text))
        
        from src.api.sample.models.sample import SampleRepository
        repository = SampleRepository()
        
        result: Row[tuple[int,str,str,datetime,datetime]] = repository.get_sample_users()
        
        expected_result = [
            (1, "john_doe", "john@example.com", datetime(2023, 1, 1, 0, 0, 0), None),
            (2, "jane_smith", "jane@example.com", datetime(2023, 1, 2, 0, 0, 0), None)
        ]

        assert len(result) == 2