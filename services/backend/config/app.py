from sanic import Sanic
from .config import Config
from .routes import setup_routes

app = Sanic(name="quTer")

app.config.update(Config().as_dict)
setup_routes(app)
