from flask import render_template
from . import errors_bp
from flask_login import current_user

@errors_bp.app_errorhandler(404)
def not_found_error(error):
    return render_template("404.html", current_user=current_user), 404

@errors_bp.app_errorhandler(500)
def internal_server_error(error):
    # In a real app, you might want to log the error
    return render_template("500.html", current_user=current_user), 500

