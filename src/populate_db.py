from src import db, create_app
from src.models import Team, Championship, Match, Odd
from datetime import datetime, timedelta
import random

def populate_db():
    app = create_app()
    with app.app_context():
        # Limpar banco
        db.drop_all()
        db.create_all()

        # Criar times
        teams = {
            'Futebol': [
                'Flamengo', 'Palmeiras', 'São Paulo', 'Santos', 'Corinthians',
                'Grêmio', 'Internacional', 'Cruzeiro', 'Atlético-MG', 'Botafogo'
            ],
            'Basquete': [
                'Flamengo', 'São Paulo', 'Franca', 'Bauru', 'Minas',
                'Pinheiros', 'Paulistano', 'Mogi', 'Brasília', 'Caxias'
            ],
            'Vôlei': [
                'Sada', 'Sesi', 'Minas', 'Suzano', 'Campinas',
                'Barueri', 'Praia', 'Brasília', 'São José', 'Osasco'
            ],
            'Tênis': [
                'Brasil Open', 'Rio Open', 'São Paulo Open', 'Salvador Open',
                'Recife Open', 'Fortaleza Open', 'Belo Horizonte Open'
            ],
            'Fórmula 1': [
                'Ferrari', 'Mercedes', 'Red Bull', 'McLaren', 'Aston Martin',
                'Alpine', 'Williams', 'Alfa Romeo', 'Haas', 'AlphaTauri'
            ]
        }

        # Criar campeonatos com ícones
        championships = {
            'Futebol': [
                ('Brasileirão', 'trophy'),
                ('Libertadores', 'trophy-fill'),
                ('Copa do Brasil', 'cup-hot'),
                ('Paulistão', 'trophy'),
                ('Carioca', 'trophy')
            ],
            'Basquete': [
                ('NBB', 'basketball'),
                ('Liga das Américas', 'basketball-fill'),
                ('Copa Intercontinental', 'trophy')
            ],
            'Vôlei': [
                ('Superliga', 'volleyball'),
                ('Mundial de Clubes', 'trophy'),
                ('Copa do Brasil', 'cup-hot')
            ],
            'Tênis': [
                ('ATP 250', 'trophy'),
                ('ATP 500', 'trophy-fill'),
                ('Grand Slam', 'trophy')
            ],
            'Fórmula 1': [
                ('GP do Brasil', 'car-front'),
                ('GP de São Paulo', 'car-front-fill'),
                ('Campeonato Mundial', 'trophy')
            ]
        }

        # Criar times no banco
        teams_db = {}
        for sport, team_list in teams.items():
            for team_name in team_list:
                team = Team(name=team_name)
                db.session.add(team)
                teams_db[team_name] = team

        # Criar campeonatos no banco
        championships_db = {}
        for sport, championship_list in championships.items():
            for champ_name, icon in championship_list:
                championship = Championship(name=champ_name, icon=icon)
                db.session.add(championship)
                championships_db[champ_name] = championship

        db.session.commit()

        # Criar partidas
        for sport, championship_list in championships.items():
            for champ_name, _ in championship_list:
                championship = championships_db[champ_name]
                sport_teams = teams[sport]
                
                # Criar 10 partidas para cada campeonato
                for i in range(10):
                    home_team = random.choice(sport_teams)
                    away_team = random.choice([t for t in sport_teams if t != home_team])
                    
                    # Data aleatória nos próximos 30 dias
                    start_time = datetime.now() + timedelta(days=random.randint(1, 30))
                    
                    match = Match(
                        championship=championship,
                        home_team=teams_db[home_team],
                        away_team=teams_db[away_team],
                        start_time=start_time
                    )
                    db.session.add(match)
                    
                    # Criar odds para cada partida
                    if sport == 'Futebol':
                        odds = [
                            ('Casa', random.uniform(1.5, 3.0)),
                            ('Empate', random.uniform(2.0, 4.0)),
                            ('Fora', random.uniform(1.5, 3.0))
                        ]
                    elif sport == 'Basquete':
                        odds = [
                            ('Casa', random.uniform(1.2, 2.0)),
                            ('Fora', random.uniform(1.2, 2.0))
                        ]
                    elif sport == 'Vôlei':
                        odds = [
                            ('Casa', random.uniform(1.2, 2.0)),
                            ('Fora', random.uniform(1.2, 2.0))
                        ]
                    elif sport == 'Tênis':
                        odds = [
                            ('Jogador 1', random.uniform(1.2, 2.0)),
                            ('Jogador 2', random.uniform(1.2, 2.0))
                        ]
                    else:  # Fórmula 1
                        odds = [
                            ('Piloto 1', random.uniform(1.2, 3.0)),
                            ('Piloto 2', random.uniform(1.2, 3.0)),
                            ('Piloto 3', random.uniform(1.2, 3.0))
                        ]
                    
                    for desc, value in odds:
                        odd = Odd(match=match, description=desc, value=round(value, 2))
                        db.session.add(odd)

        db.session.commit()

if __name__ == '__main__':
    populate_db() 