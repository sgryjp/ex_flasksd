"""API implementation."""
import flask
from random import random

bp = flask.Blueprint("api", __name__)


def _generate_random_csv():
    for i in range(1024):
        yield ",".join([f"{random():.6f}" for j in range(1024)]) + "\n"


@bp.route("/download")
def download():
    """Trigger download of the dummy data."""
    resp: flask.Response

    streaming = flask.request.args.get("streaming", "false").lower() != "false"
    if streaming:
        resp = flask.Response(_generate_random_csv())
        resp.content_length = 9_437_184  # Inform total size
    else:
        resp = flask.Response("".join([row for row in _generate_random_csv()]))
    resp.headers["X-STREAMING"] = str(streaming).lower()  # For testing
    resp.mimetype = "text/csv"

    return resp
