from flask import Blueprint
from app.routes.auth import auth_blueprint
from app.routes.index import index_blueprint

route_blueprint = Blueprint('route', __name__)

route_blueprint.register_blueprint(auth_blueprint)
route_blueprint.register_blueprint(index_blueprint)