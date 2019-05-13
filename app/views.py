from flask import render_template

from app import app

@app.route('/')
def hello():
    usuarioAutenticado = 'Gustavo'
    nomes = ['isaque', 'milena', 'daniel']
    return render_template(
        'index.html', 
        title='Desenvolvimento de Aplicações Web - INTIN 4',
        alunos=nomes,
        user=usuarioAutenticado)
