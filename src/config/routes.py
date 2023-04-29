from sanic import Sanic
from apps import blueprint


def setup_routes(app: Sanic) -> None:
    app.blueprint(blueprint)
