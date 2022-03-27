import ex_flasksd
import flask
import pytest


@pytest.fixture()
def app():
    app = ex_flasksd.create_app()

    # Setup (nothing)

    yield app

    # Clean up (nothing)


@pytest.fixture()
def client(app):
    return app.test_client()


def test_download_streaming(client):
    resp: flask.Response

    resp = client.get("/api/download?streaming=false")
    assert resp.headers.get("X-STREAMING") == "false"

    resp = client.get("/api/download?streaming=true")
    assert resp.headers.get("X-STREAMING") == "true"
