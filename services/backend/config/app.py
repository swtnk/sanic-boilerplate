from http import HTTPStatus
from sanic import Sanic
from sanic import response as sanic_response, request as sanic_request
from sanic.exceptions import NotFound
from .config import Config
from .routes import setup_routes

app = Sanic(name="quTer")

app.config.update(Config().as_dict)
setup_routes(app)


@app.exception(NotFound)
async def ignore_404s(
    request: sanic_request.types.Request, exception
) -> sanic_response.types.JSONResponse:
    return sanic_response.json(
        {"status": "error", "message": "Not Found"}, status=HTTPStatus.NOT_FOUND
    )
