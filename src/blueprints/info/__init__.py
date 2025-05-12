from flask import Blueprint

info_bp = Blueprint("info", __name__, template_folder="../../templates/info", url_prefix="/info")

from . import routes

