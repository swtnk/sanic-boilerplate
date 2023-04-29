from http import HTTPStatus
from sanic import views, response as sanic_response, request as sanic_request


class HealthCheck(views.HTTPMethodView):
    async def get(
        self, request: sanic_request.types.Request
    ) -> sanic_response.types.JSONResponse:
        return sanic_response.json({}, status=HTTPStatus.OK)
