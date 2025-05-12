from src import create_app, db
from src.models import Team, Championship, Match, Odd
from datetime import datetime, timedelta

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Times
    teams = [
        Team(name="Universidade Alpha"),
        Team(name="Universidade Beta"),
        Team(name="Leões da Montanha"),
        Team(name="Águias do Vale"),
        Team(name="Tigres Praianos"),
        Team(name="Panteras Selvagens"),
        Team(name="Basqueteiros"),
        Team(name="Vôlei Power"),
        Team(name="Xadrez Masters"),
        Team(name="Handball Force"),
        Team(name="Beach Tenis Stars"),
        Team(name="Skate Riders"),
        Team(name="eSports Pro"),
        Team(name="Tênis Club"),
        Team(name="Futsal Kings"),
        Team(name="Natação Sharks"),
        Team(name="Atletismo Speed"),
        Team(name="Rugby Bulls"),
        Team(name="Beisebol Eagles"),
        Team(name="Surfe Waves"),
        Team(name="Ciclismo Fast"),
        Team(name="Boxe Fighters"),
        Team(name="Judô Samurai"),
        Team(name="Badminton Smash"),
        Team(name="Ping Pong Spin"),
        Team(name="Corrida Flash"),
        Team(name="Ginástica Flex"),
        Team(name="Golfe Green"),
        Team(name="Automobilismo Race"),
        Team(name="Arco e Flecha Target")
    ]
    db.session.add_all(teams)
    db.session.commit()

    # Campeonatos
    campeonatos = [
        Championship(name="Campeonato Universitário de Futebol"),
        Championship(name="Campeonato Universitário de Basquete"),
        Championship(name="Campeonato Universitário de Vôlei"),
        Championship(name="Campeonato Universitário de Xadrez"),
        Championship(name="Campeonato Universitário de Handball"),
        Championship(name="Campeonato Universitário de Beach Tenis"),
        Championship(name="Campeonato Universitário de Skate"),
        Championship(name="Campeonato Universitário de eSports"),
        Championship(name="Campeonato Universitário de Tênis"),
        Championship(name="Campeonato Universitário de Futsal"),
        Championship(name="Campeonato Universitário de Natação"),
        Championship(name="Campeonato Universitário de Atletismo"),
        Championship(name="Campeonato Universitário de Rugby"),
        Championship(name="Campeonato Universitário de Beisebol"),
        Championship(name="Campeonato Universitário de Surfe"),
        Championship(name="Campeonato Universitário de Ciclismo"),
        Championship(name="Campeonato Universitário de Boxe"),
        Championship(name="Campeonato Universitário de Judô"),
        Championship(name="Campeonato Universitário de Badminton"),
        Championship(name="Campeonato Universitário de Ping Pong"),
        Championship(name="Campeonato Universitário de Corrida"),
        Championship(name="Campeonato Universitário de Ginástica"),
        Championship(name="Campeonato Universitário de Golfe"),
        Championship(name="Campeonato Universitário de Automobilismo"),
        Championship(name="Campeonato Universitário de Arco e Flecha")
    ]
    db.session.add_all(campeonatos)
    db.session.commit()

    # Partidas e Odds (exemplo para alguns esportes)
    matches = []
    odds = []
    now = datetime.now()
    for i, champ in enumerate(campeonatos):
        for j in range(2):
            home = teams[(i+j)%len(teams)]
            away = teams[(i+j+1)%len(teams)]
            match = Match(
                championship_id=champ.id,
                home_team_id=home.id,
                away_team_id=away.id,
                start_time=now + timedelta(days=i, hours=j*2),
                status="Agendado"
            )
            db.session.add(match)
            db.session.flush()  # Para pegar o id
            odds.append(Odd(match_id=match.id, description=f"{home.name} Vence", value=round(1.5 + i*0.1, 2)))
            odds.append(Odd(match_id=match.id, description="Empate", value=round(2.5 + i*0.1, 2)))
            odds.append(Odd(match_id=match.id, description=f"{away.name} Vence", value=round(2.0 + i*0.1, 2)))
    db.session.add_all(odds)
    db.session.commit()

    print("Banco de dados populado com muitos esportes, times e partidas!") 