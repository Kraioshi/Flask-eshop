from flask import Blueprint, render_template, url_for

redirect_bp = Blueprint('redirect', __name__)


@redirect_bp.route('/redirect_page')
def redirect_page():
    message = 'Redirecting!'
    redirect_url = url_for('index.index')
    return render_template('redirect/redirect_page.html', message=message, redirect_url=redirect_url)
