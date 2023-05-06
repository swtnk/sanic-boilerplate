from sanic import Blueprint
from . import views

blueprint = Blueprint(name="public_bp", version=1, url_prefix="public")

blueprint.add_route(views.HealthCheck.as_view(), uri="/health", name="health_check")
blueprint.add_route(views.ListAvailableUrl.as_view(), uri="/urls", name="urls")
