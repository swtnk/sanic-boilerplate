from http import HTTPStatus
from sanic import views, response as sanic_response, request as sanic_request


class HealthCheck(views.HTTPMethodView):
    async def get(
        self, request: sanic_request.types.Request
    ) -> sanic_response.types.JSONResponse:
        return sanic_response.json({}, status=HTTPStatus.OK)


class ListAvailableUrl(views.HTTPMethodView):
    async def get(
        self, request: sanic_request.types.Request
    ) -> sanic_response.types.JSONResponse:
        if request.app.debug:
            urls = [
                request.app.url_for(url.name, _external=True, _server=request.host)
                for url in request.app.router.routes_all.values()
            ]
            return sanic_response.json({"urls": urls}, indent=4, status=HTTPStatus.OK)
        return sanic_response.json({}, status=HTTPStatus.NOT_FOUND)
