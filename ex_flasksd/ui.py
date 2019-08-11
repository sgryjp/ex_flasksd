"""UI implementation."""
import flask

bp = flask.Blueprint("ui", __name__)


@bp.route("/")
def index():
    """Home page."""
    return flask.render_template("index.html")
