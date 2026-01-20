"""
Basic API tests for Market Stats API.

Run with: pytest test_api.py
"""

from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from server.main import app

client = TestClient(app)


def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_list_users():
    """Test listing users endpoint."""
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_evaluate_endpoint_exists():
    """Test that the evaluate endpoint exists (will fail without API key in tests)."""
    response = client.get("/evaluate/AAPL")
    # Should return 200 or 500 (if API key issue), but not 404
    assert response.status_code in [200, 500]


def test_invalid_stock_symbol():
    """Test that invalid stock symbols are rejected."""
    # Test with lowercase (should fail validation)
    response = client.get("/probabilities?stock_symbol=aapl")
    assert response.status_code == 422  # Validation error
    
    # Test with empty string
    response = client.get("/probabilities?stock_symbol=")
    assert response.status_code == 422  # Validation error
    
    # Test with too long symbol
    response = client.get("/probabilities?stock_symbol=TOOLONGSYMBOL")
    assert response.status_code == 422  # Validation error


def test_valid_stock_symbol():
    """Test that valid stock symbols are accepted."""
    response = client.get("/probabilities?stock_symbol=AAPL")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
