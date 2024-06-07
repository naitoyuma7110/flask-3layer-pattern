from abc import ABC, abstractmethod
from datetime import datetime
from dataclasses import dataclass
from injector import inject
from api.models.sample import (ISampleRepository, User)
from sqlalchemy import String, Integer, DateTime, distinct

@dataclass
class Sample:
    sample:str | None = None
    username:str  = "デフォルトname"
    email:str | None = None
    created_at:datetime | str | None = None
    deleted_at:datetime | str | None = None
    
@dataclass
class Samples:
    samples:list[Sample]

class ISampleService(ABC):
    
    @abstractmethod
    def get_sample(self, text:str) -> Sample:
        pass

class SampleService(ISampleService):
    @inject
    def __init__(self, sample_repository:ISampleRepository):
        super().__init__()
        self.sample_repository = sample_repository
        
    def get_sample(self, text) -> list[Sample]:
        
        text = text
        
        user_models:list[User] = self.sample_repository.get_sample_users()
        
        samples = [Sample(
            sample=text,
            username=user_model.username,
            email=user_model.email,
            created_at=user_model.created_at,
            deleted_at=user_model.deleted_at
        ) for user_model in user_models]
        
        return Samples(samples)
