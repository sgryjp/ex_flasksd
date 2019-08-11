"""ex_flasksd package."""
import flask

__version__ = "19.8.12"


def create_app():
    """Create a Flask application."""
    app = flask.Flask(__name__)

    import ex_flasksd.ui
    import ex_flasksd.api
    app.register_blueprint(ex_flasksd.ui.bp, url_prefix="/")
    app.register_blueprint(ex_flasksd.api.bp, url_prefix="/api")

    return app
