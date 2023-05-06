from http import HTTPStatus
from sanic import views
from sanic import request as sanic_request, response as sanic_response


class Home(views.HTTPMethodView):
    def get(
        self, request: sanic_request.types.Request
    ) -> sanic_response.types.JSONResponse:
        data = {"app_name": request.app.name, "version": 1.0}
        return sanic_response.json(data, indent=4, status=HTTPStatus.OK)
