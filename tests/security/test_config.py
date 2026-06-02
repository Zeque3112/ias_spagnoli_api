from app.init import create_app


def test_debug_is_boolean():
    app = create_app()

    assert isinstance(app.config["DEBUG"], bool)

def test_environment_is_valid():
    app = create_app()

    assert app.config["ENV"] in [
        "development",
        "qa",
        "production"
    ]