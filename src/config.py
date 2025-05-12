import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "uma-chave-secreta-muito-dificil-de-adivinhar"
    # Configurações do SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///campus_bet.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Outras configurações da aplicação podem ser adicionadas aqui
    # Exemplo: Configurações de base de dados (quando não for mock)
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///app.db"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

