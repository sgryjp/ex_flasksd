"""Entry point of the package."""
import ex_flasksd
import waitress


if __name__ == "__main__":
    waitress.serve(ex_flasksd.create_app())
