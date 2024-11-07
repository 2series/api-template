import pytest
from fastapi.testclient import TestClient
from fastapi import status

class TestHealthCheck:
    """Test cases for health check endpoint"""
    
    def test_health_check(self, client: TestClient):
        """Test successful health check"""
        response = client.get("/api/v1/health")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"status": "healthy"}

class TestProtectedRoutes:
    """Test cases for protected routes"""
    
    def test_protected_route_without_token(self, client: TestClient):
        """Test protected route access without token"""
        response = client.get("/api/v1/protected")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "detail" in response.json()
        assert response.headers.get("WWW-Authenticate") == "Bearer"

    def test_protected_route_with_valid_token(self, client: TestClient, token_headers: dict):
        """Test protected route access with valid token"""
        response = client.get("/api/v1/protected", headers=token_headers)
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["message"] == "This is a protected route"
        assert "user" in response.json()

    def test_protected_route_with_invalid_token(
        self, client: TestClient, unauthorized_token_headers: dict
    ):
        """Test protected route access with invalid token"""
        response = client.get("/api/v1/protected", headers=unauthorized_token_headers)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "detail" in response.json() 