from flask import Flask
from flask_login import LoginManager
from src.config import Config
import os
import sys
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Adicionar o diretório pai de 'src' ao sys.path para permitir importações como 'from src.blueprints...'
# Isto é crucial se main.py estiver dentro de src e for executado diretamente, ou se a app for criada aqui.
# No entanto, o template create_flask_app geralmente lida com isso de outra forma.
# A linha sys.path.insert(0, os.path.dirname(os.path.dirname(__file__))) no main.py do template é para quando main.py está em src.

db = SQLAlchemy()
migrate = Migrate()

login_manager = LoginManager()
login_manager.login_view = "auth.login" # Rota para onde o utilizador é redirecionado se tentar aceder a uma página protegida sem estar logado
login_manager.login_message_category = "info" # Categoria da mensagem flash para o login_required

# Função para criar a aplicação Flask
def create_app(config_class=Config):
    # Assegurar que o diretório 'src' está no sys.path para importações corretas dos blueprints
    # Isto é importante se o __init__.py estiver no mesmo nível que 'blueprints', 'models', etc.
    # e a app for criada a partir de um main.py no diretório raiz do projeto (fora de 'src')
    # Se main.py está em 'src', o sys.path.insert no main.py já deve tratar disso.
    
    # Se este __init__.py estiver em /home/ubuntu/campus_bet_project/campus_bet/src/
    # e os blueprints estiverem em /home/ubuntu/campus_bet_project/campus_bet/src/blueprints/
    # as importações relativas como from .blueprints.auth import auth_bp devem funcionar.

    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(config_class)

    # Inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Importar e registar Blueprints
    from src.blueprints.auth import auth_bp
    from src.blueprints.main import main_bp
    from src.blueprints.bets import bets_bp
    from src.blueprints.profile import profile_bp
    from src.blueprints.ranking import ranking_bp
    from src.blueprints.info import info_bp
    from src.blueprints.errors import errors_bp # Manipuladores de erro
    from src.utils import gravatar_url
    from src.models import User

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(bets_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(ranking_bp)
    app.register_blueprint(info_bp)
    app.register_blueprint(errors_bp)
    
    app.jinja_env.globals['gravatar_url'] = gravatar_url

    # Bootstrap-Flask (opcional, mas útil se não estiver a usar CDN para tudo)
    # from flask_bootstrap import Bootstrap
    # bootstrap = Bootstrap(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

# Importar modelos para que o Flask-Migrate detecte as tabelas
from src import models

