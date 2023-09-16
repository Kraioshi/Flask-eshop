from flask import Blueprint, render_template

not_found_bp = Blueprint("not_found", __name__)


@not_found_bp.errorhandler(404)
def page_not_found(e):
    print("oopstie")
    return render_template('errors/404.html'), 404
