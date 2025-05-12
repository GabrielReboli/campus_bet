import datetime

# Mock Users
# Simulação de password_hash (numa aplicação real, seriam hashes gerados por Werkzeug)
users_mock = [
    {
        "id": 1, "nome": "João", "sobrenome": "Silva", "email": "joao.silva@example.com", 
        "password_hash": "pbkdf2:sha256:150000$abcdef$1234567890abcdef1234567890abcdef", # Exemplo, não usar em produção
        "cpf": "11122233344", "data_nascimento": datetime.date(1995, 5, 10), 
        "universidade": "Universidade Alpha", "saldo": 150.75,
        "data_criacao": datetime.datetime(2024, 1, 15, 10, 0, 0),
        "ultima_atividade": datetime.datetime(2025, 5, 10, 14, 30, 0),
        "avatar_url": "https://via.placeholder.com/150/007bff/ffffff?Text=JS",
        "stats": {
            "taxa_acerto": 65.5, "total_apostado": 1250.00, "rendimento": 250.50,
            "maior_odd_ganha": 5.50, "esporte_mais_jogado": "Futebol"
        }
    },
    {
        "id": 2, "nome": "Maria", "sobrenome": "Oliveira", "email": "maria.oliveira@example.com", 
        "password_hash": "pbkdf2:sha256:150000$ghijkl$0987654321fedcba0987654321fedcba",
        "cpf": "55566677788", "data_nascimento": datetime.date(1998, 8, 22), 
        "universidade": "Universidade Beta", "saldo": 320.00,
        "data_criacao": datetime.datetime(2024, 3, 1, 11, 0, 0),
        "ultima_atividade": datetime.datetime(2025, 5, 11, 9, 15, 0),
        "avatar_url": "https://via.placeholder.com/150/28a745/ffffff?Text=MO",
        "stats": {
            "taxa_acerto": 72.0, "total_apostado": 2100.00, "rendimento": 750.00,
            "maior_odd_ganha": 8.20, "esporte_mais_jogado": "Basquete"
        }
    },
    {
        "id": 3, "nome": "Carlos", "sobrenome": "Pereira", "email": "carlos.pereira@example.com", 
        "password_hash": "pbkdf2:sha256:150000$mnopqr$abcdef1234567890abcdef1234567890",
        "cpf": "99988877766", "data_nascimento": datetime.date(1990, 1, 30), 
        "universidade": "Universidade Gama", "saldo": 50.20,
        "data_criacao": datetime.datetime(2024, 2, 10, 12, 0, 0),
        "ultima_atividade": datetime.datetime(2025, 5, 9, 18, 0, 0),
        "avatar_url": "https://via.placeholder.com/150/ffc107/000000?Text=CP",
        "stats": {
            "taxa_acerto": 50.0, "total_apostado": 800.00, "rendimento": -150.00,
            "maior_odd_ganha": 3.10, "esporte_mais_jogado": "Vôlei"
        }
    }
]

# Mock Sports
sports_mock = [
    {"id": 1, "name": "Futebol"},
    {"id": 2, "name": "Vôlei"},
    {"id": 3, "name": "Basquete"},
    {"id": 4, "name": "Xadrez"},
    {"id": 5, "name": "Handball"},
    {"id": 6, "name": "Beach Tenis"},
    {"id": 7, "name": "Skate"},
    {"id": 8, "name": "eSports"}
]

# Mock Events
events_mock = [
    {
        "id": 1, "sport_id": 1, "sport_name": "Futebol",
        "name_event": "Universidade Alpha vs Universidade Beta - Final", 
        "data_hora": datetime.datetime(2025, 5, 15, 19, 0, 0), 
        "status": "Agendado", "resultado_final": None
    },
    {
        "id": 2, "sport_id": 3, "sport_name": "Basquete",
        "name_event": "Leões da Montanha vs Águias do Vale - Semifinal", 
        "data_hora": datetime.datetime(2025, 5, 16, 20, 30, 0), 
        "status": "Agendado", "resultado_final": None
    },
    {
        "id": 3, "sport_id": 2, "sport_name": "Vôlei",
        "name_event": "Tigres Praianos vs Panteras Selvagens", 
        "data_hora": datetime.datetime(2025, 5, 12, 10, 0, 0), 
        "status": "Finalizado", "resultado_final": "3-1"
    },
    {
        "id": 4, "sport_id": 8, "sport_name": "eSports",
        "name_event": "Campeonato InterUniversitário de LoL - Grande Final", 
        "data_hora": datetime.datetime(2025, 5, 18, 14, 0, 0), 
        "status": "Agendado", "resultado_final": None
    }
]

# Mock Odds
odds_mock = [
    {"id": 1, "event_id": 1, "tipo_odd": "Alpha Vence", "valor_odd": 1.85},
    {"id": 2, "event_id": 1, "tipo_odd": "Empate", "valor_odd": 3.20},
    {"id": 3, "event_id": 1, "tipo_odd": "Beta Vence", "valor_odd": 4.50},
    {"id": 4, "event_id": 2, "tipo_odd": "Leões Vencem", "valor_odd": 1.50},
    {"id": 5, "event_id": 2, "tipo_odd": "Águias Vencem", "valor_odd": 2.50},
    {"id": 6, "event_id": 3, "tipo_odd": "Tigres 3-0", "valor_odd": 2.20},
    {"id": 7, "event_id": 3, "tipo_odd": "Panteras 3-0", "valor_odd": 5.00},
    {"id": 8, "event_id": 4, "tipo_odd": "Time Vermelho Vence", "valor_odd": 1.90},
    {"id": 9, "event_id": 4, "tipo_odd": "Time Azul Vence", "valor_odd": 1.90},
]

# Mock Bets
bets_mock = [
    {
        "id": 1, "user_id": 1, "event_id": 3, "event_name": "Tigres Praianos vs Panteras Selvagens", "sport_name": "Vôlei",
        "odd_id": 6, "bet_type": "Tigres 3-0", "valor_apostado": 20.00, "odd_value": 2.20,
        "potential_return": 44.00, "amount_won": 44.00,
        "data_aposta": datetime.datetime(2025, 5, 11, 15, 0, 0), 
        "status": "Ganha", "date_resolved": datetime.datetime(2025, 5, 12, 12, 0, 0)
    },
    {
        "id": 2, "user_id": 1, "event_id": 1, "event_name": "Universidade Alpha vs Universidade Beta - Final", "sport_name": "Futebol",
        "odd_id": 1, "bet_type": "Alpha Vence", "valor_apostado": 50.00, "odd_value": 1.85,
        "potential_return": 92.50, "amount_won": None,
        "data_aposta": datetime.datetime(2025, 5, 13, 10, 0, 0), 
        "status": "Aberta", "date_resolved": None
    },
    {
        "id": 3, "user_id": 2, "event_id": 2, "event_name": "Leões da Montanha vs Águias do Vale - Semifinal", "sport_name": "Basquete",
        "odd_id": 5, "bet_type": "Águias Vencem", "valor_apostado": 100.00, "odd_value": 2.50,
        "potential_return": 250.00, "amount_won": None,
        "data_aposta": datetime.datetime(2025, 5, 14, 9, 30, 0), 
        "status": "Aberta", "date_resolved": None
    },
     {
        "id": 4, "user_id": 1, "event_id": 2, "event_name": "Leões da Montanha vs Águias do Vale - Semifinal", "sport_name": "Basquete",
        "odd_id": 4, "bet_type": "Leões Vencem", "valor_apostado": 10.00, "odd_value": 1.50,
        "potential_return": 15.00, "amount_won": 0.00,
        "data_aposta": datetime.datetime(2025, 5, 10, 11,0,0), 
        "status": "Perdida", "date_resolved": datetime.datetime(2025, 5, 11, 22,0,0)
    }
]

def get_user_by_id(user_id):
    for user in users_mock:
        if user["id"] == user_id:
            # Adicionar nome completo para facilitar no template
            user["nome_completo"] = f"{user['nome']} {user['sobrenome']}"
            return user
    return None

def get_user_by_email(email):
    for user in users_mock:
        if user["email"] == email:
            user["nome_completo"] = f"{user['nome']} {user['sobrenome']}"
            return user
    return None

def get_bets_by_user_id(user_id):
    user_bets = []
    for bet in bets_mock:
        if bet["user_id"] == user_id:
            # Renomear campos para consistência com templates
            bet_display = bet.copy()
            bet_display["amount_staked"] = bet_display.pop("valor_apostado")
            bet_display["date_placed"] = bet_display.pop("data_aposta")
            user_bets.append(bet_display)
    return sorted(user_bets, key=lambda b: b["date_placed"], reverse=True)

def get_open_bets_by_user_id(user_id):
    return [bet for bet in get_bets_by_user_id(user_id) if bet["status"] == "Aberta"]

def get_resolved_bets_by_user_id(user_id):
    return [bet for bet in get_bets_by_user_id(user_id) if bet["status"] != "Aberta"]


