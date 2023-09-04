from flask import Blueprint
from . import login, register, logout

auth_bp = Blueprint('auth', __name__)
