from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# Configurações
app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui'

# Dados do portfólio (em produção, isso viria de um banco de dados)
PORTFOLIO_DATA = {
    'nome':
    'Igor',
    'titulo':
    'Graduando em Estatística & Entusiasta de Programação',
    'sobre':
    'Sou estudante de Estatística no 1º semestre, apaixonado por dados e programação. Estou começando minha jornada no mundo da tecnologia e análise de dados.',
    'anos_experiencia':
    0.2,
    'projetos_concluidos':
    2,
    'habilidades': [{
        'nome': 'R',
        'nivel': 70,
        'icone': '📊'
    }, {
        'nome': 'Python',
        'nivel': 45,
        'icone': '🐍'
    }, {
        'nome': 'HTML/CSS',
        'nivel': 40,
        'icone': '🎨'
    }, {
        'nome': 'Estatística',
        'nivel': 60,
        'icone': '📈'
    }, {
        'nome': 'Excel',
        'nivel': 75,
        'icone': '📋'
    }, {
        'nome': 'Git',
        'nivel': 35,
        'icone': '📁'
    }],
    'projetos': [{
        'nome':
        'Aplicativo em R',
        'descricao':
        'Primeiro projeto desenvolvido em R para análise estatística de dados.',
        'tecnologias': ['R', 'Estatística'],
        'link':
        'https://github.com/Igor-ht-1/Trabalho-espaco-das-profissoes-Nato-Igor'
    }, {
        'nome': 'Portfólio Web',
        'descricao':
        'Este portfólio pessoal desenvolvido em Flask para aprender web development.',
        'tecnologias': ['Python', 'Flask', 'HTML', 'CSS'],
        'link': '#'
    }, {
        'nome': 'Projeto Futuro com Amigo (Nato🛹💻)',
        'descricao':
        'Projeto em desenvolvimento colaborativo focado em IA (em breve!).',
        'tecnologias': ['C', 'Python', 'Inteligência Artificial'],
        'link': '#'
    }],
    'contatos': {
        'email': 'igor@exemplo.com',
        'github': 'https://github.com/igor',
        'linkedin': 'https://linkedin.com/in/igor'
    }
}


@app.route('/')
def home():
    """Página principal do portfólio"""
    return render_template('index.html', dados=PORTFOLIO_DATA)


@app.route('/api/stats')
def api_stats():
    """API para estatísticas do portfólio"""
    stats = {
        'projetos_concluidos': PORTFOLIO_DATA['projetos_concluidos'],
        'anos_experiencia': PORTFOLIO_DATA['anos_experiencia'],
        'tecnologias_dominadas': len(PORTFOLIO_DATA['habilidades']),
        'ultimo_update': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return jsonify(stats)


@app.route('/api/projetos')
def api_projetos():
    """API para lista de projetos"""
    return jsonify(PORTFOLIO_DATA['projetos'])


@app.route('/api/habilidades')
def api_habilidades():
    """API para lista de habilidades"""
    return jsonify(PORTFOLIO_DATA['habilidades'])


@app.errorhandler(404)
def page_not_found(e):
    """Página de erro 404 personalizada"""
    return render_template('404.html'), 404


if __name__ == '__main__':
    # Para desenvolvimento, use debug=True
    app.run(host='0.0.0.0', port=3000, debug=True)
