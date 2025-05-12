from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from . import profile_bp
from src.models import User, Bet, Odd, Match, Championship
from collections import Counter

@profile_bp.route("/")
@login_required
def view_my_profile():
    user = current_user
    bets = Bet.query.filter_by(user_id=user.id).all()
    saldo = user.balance or 0
    total_apostado = sum(b.amount for b in bets)
    rendimento = sum((b.amount_won or 0) - b.amount for b in bets if b.status == "Ganha")
    maior_odd = max([b.odd.value for b in bets if b.status == "Ganha"], default=0)
    # Esporte mais apostado (campeonato mais frequente)
    campeonatos = [b.odd.match.championship.name for b in bets]
    esporte_mais_jogado = Counter(campeonatos).most_common(1)[0][0] if campeonatos else "N/A"
    ultimas_apostas = sorted(bets, key=lambda b: b.placed_at, reverse=True)[:5]
    return render_template(
        "view_profile.html",
        user=user,
        saldo=saldo,
        total_apostado=total_apostado,
        rendimento=rendimento,
        maior_odd=maior_odd,
        esporte_mais_jogado=esporte_mais_jogado,
        ultimas_apostas=ultimas_apostas
    )

@profile_bp.route("/<string:username>")
@login_required
def view_user_profile(username):
    # Busca usuário pelo username no banco de dados
    user = User.query.filter_by(username=username).first()
    if not user:
        flash(f"Perfil para o usuário {username} não encontrado.", "warning")
        return redirect(url_for("main.index"))
    is_own_profile = (current_user.id == user.id)
    return render_template("view_profile.html", user=user, is_own_profile=is_own_profile)

@profile_bp.route("/editar", methods=["GET", "POST"])
@login_required
def edit_profile():
    # Aqui você pode implementar a edição do perfil real futuramente
    flash("Funcionalidade de edição de perfil ainda não implementada.", "info")
    return redirect(url_for("profile.view_my_profile"))

# Need a simple template for edit_profile.html
# This should be created in templates/profile/edit_profile.html

