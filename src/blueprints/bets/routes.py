from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
import datetime

from . import bets_bp
from src.forms import BetSubmissionForm
from src.models import db, Match, Odd, Bet, User, Championship

@bets_bp.route("/minhas")
@login_required
def my_bets():
    user_id = int(current_user.get_id())
    open_bets_data = Bet.query.filter_by(user_id=user_id, status="Aberta").all()
    resolved_bets_data = Bet.query.filter(Bet.user_id==user_id, Bet.status!="Aberta").all()
    return render_template("my_bets.html", title="Minhas Apostas", 
                           open_bets=open_bets_data, 
                           resolved_bets=resolved_bets_data, 
                           current_user=current_user)

@bets_bp.route("/fazer-aposta/<int:match_id>", methods=["GET", "POST"])
@login_required
def place_bet(match_id):
    match = Match.query.get(match_id)
    if not match:
        flash("Evento não encontrado.", "danger")
        return redirect(url_for("main.index"))

    event_odds = Odd.query.filter_by(match_id=match_id).all()
    form = BetSubmissionForm()
    choices_list = [(odd.id, f"{odd.description} ({odd.value})") for odd in event_odds]
    form.selected_odd_id.choices = choices_list

    if form.validate_on_submit():
        user_id = int(current_user.get_id())
        selected_odd = Odd.query.get(form.selected_odd_id.data)
        amount = float(form.amount_staked.data)
        user = User.query.get(user_id)
        if not selected_odd:
            flash("Odd não encontrada.", "danger")
            return redirect(url_for("bets.place_bet", match_id=match_id))
        if user.balance < amount:
            flash("Saldo insuficiente para realizar esta aposta.", "warning")
            return redirect(url_for("bets.place_bet", match_id=match_id))
        user.balance -= amount
        bet = Bet(user_id=user_id, odd_id=selected_odd.id, amount=amount, status="Aberta")
        db.session.add(bet)
        db.session.commit()
        flash(f"Aposta de R$ {amount} em {selected_odd.description} para o evento realizada com sucesso!", "success")
        return redirect(url_for("bets.my_bets"))

    return render_template("place_bet_mock.html", title=f"Apostar em: {match.home_team.name} vs {match.away_team.name}", 
                           form=form, event=match, event_odds=event_odds, current_user=current_user)

# Need a simple template for place_bet_mock.html
# This should be created in templates/bets/place_bet_mock.html

@bets_bp.route("/partidas")
@login_required
def list_matches():
    esporte = request.args.get('esporte')
    campeonatos = Championship.query.all()
    if esporte:
        campeonato = Championship.query.filter_by(name=esporte).first()
        matches = Match.query.filter(Match.championship_id==campeonato.id, Match.start_time >= datetime.datetime.now()).order_by(Match.start_time).all() if campeonato else []
    else:
        matches = Match.query.filter(Match.start_time >= datetime.datetime.now()).order_by(Match.start_time).all()
    return render_template("list_matches.html", matches=matches, campeonatos=campeonatos, esporte_selecionado=esporte)

