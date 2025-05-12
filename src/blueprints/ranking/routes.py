from flask import render_template
from flask_login import current_user

from . import ranking_bp
from src.mock_data import users_mock # Using mock data

@ranking_bp.route("/")
def show_ranking():
    # Sort users by a mock score or rendimento for ranking
    # For this mock, let's sort by "rendimento" from their stats if available
    # Ensure stats and rendimento exist to avoid errors
    ranked_users = sorted(
        [u for u in users_mock if u.get("stats") and u["stats"].get("rendimento") is not None],
        key=lambda x: x["stats"]["rendimento"],
        reverse=True
    )
    return render_template("ranking.html", title="Ranking de Apostadores", ranked_users=ranked_users, current_user=current_user)

