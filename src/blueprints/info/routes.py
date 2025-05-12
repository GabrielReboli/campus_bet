from flask import render_template
from flask_login import current_user

from . import info_bp

# Mock data for articles (could be moved to mock_data.py if more complex)
mock_articles = [
    {
        "title": "Como apostar na Campus.BET",
        "date": "10 de Maio, 2025",
        "summary": "Se você é novo por aqui, este guia rápido irá mostrar como é fácil começar a apostar nos seus times universitários favoritos. Desde o cadastro até a sua primeira aposta, cobrimos tudo!",
        "content_list": [
            "Crie sua conta gratuitamente.",
            "Faça seu primeiro depósito (simulado).",
            "Navegue pelos esportes e eventos disponíveis.",
            "Escolha suas odds e adicione ao bilhete de apostas.",
            "Confirme sua aposta e torça!"
        ],
        "type": "tutorial"
    },
    {
        "title": "Entendendo as Odds: O que são e como funcionam?",
        "date": "08 de Maio, 2025",
        "summary": "As odds (cotações) são o coração das apostas esportivas. Elas indicam a probabilidade de um evento acontecer e o quanto você pode ganhar. Neste artigo, desmistificamos as odds para você.",
        "content_list": [
            "Odds Decimais (Europeias)",
            "Odds Fracionárias (Britânicas)",
            "Odds Americanas (Moneyline)"
        ],
        "additional_text": "Na Campus.BET, utilizamos o formato decimal por ser o mais intuitivo para a maioria dos apostadores.",
        "type": "dica"
    },
    {
        "title": "Estratégias Básicas para Apostas em Futebol Universitário",
        "date": "05 de Maio, 2025",
        "summary": "Apostar em futebol pode ser emocionante e lucrativo se você tiver uma boa estratégia. Confira algumas dicas para iniciantes focadas no cenário universitário:",
        "content_list": [
            "Analise o desempenho recente das equipes.",
            "Considere o fator \"casa\" e \"visitante\".",
            "Fique de olho em desfalques e jogadores chave.",
            "Não aposte com o coração, use a razão!"
        ],
        "additional_text": "Lembre-se, aposte com responsabilidade.",
        "type": "estrategia"
    }
]

@info_bp.route("/dicas")
def show_tips_tutorials():
    # For the mock, we just pass the static articles defined above
    return render_template("tips.html", title="Dicas e Tutoriais", articles=mock_articles, current_user=current_user)

@info_bp.route("/noticias") # Mock route as per todo.md
def show_news():
    # Placeholder for news, can reuse tips.html or create a new one
    flash("Página de notícias ainda em construção.", "info")
    return render_template("tips.html", title="Notícias", articles=[], current_user=current_user) # Empty articles for now

@info_bp.route("/ajuda")
def help():
    return render_template("info/help.html", title="Ajuda", current_user=current_user)

@info_bp.route("/ajuda/<category>")
def help_category(category):
    # Você pode personalizar o conteúdo de cada categoria depois
    return render_template("info/help_category.html", category=category, current_user=current_user)

