from flask import Blueprint

ranking_bp = Blueprint("ranking", __name__, template_folder="../../templates/ranking", url_prefix="/ranking")

from . import routes

