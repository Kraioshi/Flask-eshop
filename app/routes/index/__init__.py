from flask import Blueprint
from app.routes.index import index_blueprint

core_blueprint = Blueprint('auth', __name__)

core_blueprint.register_blueprint(index_blueprint)



