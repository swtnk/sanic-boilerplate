from sanic import Sanic
from apps import blueprint
from . import views


def setup_routes(app: Sanic) -> None:
    app.add_route(views.Home.as_view(), "/", name="home")
    app.blueprint(blueprint)
