from app.main import app


def test_health():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_portfolio():
    client = app.test_client()
    resp = client.get("/api/portfolio/2")
    assert resp.status_code == 200
    assert resp.get_json()["nav"] == 103.0
