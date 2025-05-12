from flask import Blueprint

bets_bp = Blueprint("bets", __name__, template_folder="../../templates/bets", url_prefix="/apostas")

from . import routes

