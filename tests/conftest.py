import pytest
from typing import Generator, AsyncGenerator
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import get_settings

settings = get_settings()

@pytest.fixture
def client() -> Generator:
    """Fixture that creates a test client instance"""
    with TestClient(app) as test_client:
        yield test_client

@pytest.fixture
def test_user() -> dict:
    """Fixture that returns a test user data"""
    return {
        "username": "test_user",
        "email": "test@example.com",
        "is_active": True,
        "is_superuser": False
    }

@pytest.fixture
def token_headers(test_user: dict) -> dict:
    """Fixture that returns authorization headers with test token"""
    return {"Authorization": f"Bearer fake_test_token"}

@pytest.fixture
def unauthorized_token_headers() -> dict:
    """Fixture that returns invalid authorization headers"""
    return {"Authorization": "Bearer invalid_token"} 