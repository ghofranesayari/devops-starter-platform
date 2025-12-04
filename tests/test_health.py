import os
import sys

# Add the project root (devops-starter-platform) to Python path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from app.main import create_app


def test_health_endpoint():
    """
    This test checks that:
    - /health returns HTTP 200
    - Response JSON contains {"status": "ok"}
    """
    app = create_app()
    client = app.test_client()

    response = client.get("/health")
    assert response.status_code == 200

    data = response.get_json()
    assert data["status"] == "ok"
