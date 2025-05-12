from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from src import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=True)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy=True)
    balance = db.Column(db.Float, default=50.0)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Post {self.title}>'

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    def __repr__(self):
        return f'<Team {self.name}>'

class Championship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    icon = db.Column(db.String(50), nullable=False, default='trophy')
    def __repr__(self):
        return f'<Championship {self.name}>'

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    championship_id = db.Column(db.Integer, db.ForeignKey('championship.id'), nullable=False)
    home_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='Agendado')
    result = db.Column(db.String(50), nullable=True)
    championship = db.relationship('Championship', backref='matches')
    home_team = db.relationship('Team', foreign_keys=[home_team_id])
    away_team = db.relationship('Team', foreign_keys=[away_team_id])
    def __repr__(self):
        return f'<Match {self.home_team_id} vs {self.away_team_id}>'

class Odd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float, nullable=False)
    match = db.relationship('Match', backref='odds')
    def __repr__(self):
        return f'<Odd {self.description} ({self.value})>'

class Bet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    odd_id = db.Column(db.Integer, db.ForeignKey('odd.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    placed_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Aberta')
    amount_won = db.Column(db.Float, nullable=True)
    user = db.relationship('User', backref='bets')
    odd = db.relationship('Odd', backref='bets')
    def __repr__(self):
        return f'<Bet {self.id}>' 