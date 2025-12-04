import os
import sys

# --- Make "app" package importable (same trick as in test_health.py)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from app.main import create_app


def test_config_endpoint(monkeypatch):
    """
    Given some environment variables,
    /config should expose them correctly in JSON.
    """
    # Arrange: set fake env vars for this test only
    monkeypatch.setenv("APP_ENV", "test")
    monkeypatch.setenv("APP_VERSION", "0.0.1-test")

    app = create_app()
    client = app.test_client()

    # Act
    response = client.get("/config")

    # Assert
    assert response.status_code == 200

    data = response.get_json()
    assert data["env"] == "test"
    assert data["version"] == "0.0.1-test"
