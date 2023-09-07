from flask import Blueprint, render_template, url_for, request

redirect_bp = Blueprint('redirect', __name__)


@redirect_bp.route('/redirect_page')
def redirect_home():
    message = request.args.get('message', 'Just a moment!')
    redirect_url = url_for('index.index')
    return render_template('redirect/redirect_page.html', message=message, redirect_url=redirect_url)
