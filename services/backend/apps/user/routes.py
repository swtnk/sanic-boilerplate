from sanic import Blueprint
from . import views

blueprint = Blueprint(name="user_bp", version=1, url_prefix="user")

blueprint.add_route(views.Me.as_view(), uri="/me", name="logged_in_user")
