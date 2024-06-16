import pytest

@pytest.fixture
def session(app):
    with app.app_context():
        
        from base.database import get_session
        session = get_session()
        
        yield session
        
        session.rollback()
        session.close() 