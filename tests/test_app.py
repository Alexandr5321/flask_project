from app.app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == { "status": "ok" }

def test_info():
    client = app.test_client()
    
    response = client.get("/info")

    assert response.json == { "app": "flask_project",
                              "version": "1.0" }

def test_version():
    client = app.test_client()

    response = client.get("/version")

    assert response.json == { "version": "1.0" }
