from flask import render_template, request

from app import app

posts = []

@app.route('/')
def hello():
    usuarioAutenticado = 'Gustavo'
    nomes = ['isaque', 'milena', 'daniel']
    return render_template(
        'index.html', 
        title='Desenvolvimento de Aplicações Web - INTIN 4',
        alunos=nomes,
        user=usuarioAutenticado)

@app.route('/form', methods=['POST', 'GET'])
def helloForm():
    if request.method == 'POST':
        email = request.form['email']
        if 'status' in request.form:
            status = request.form['status']
        else:
            status = 'off'
        msg = request.form['msg']
        return render_template(
            'form_view.html', 
            email=email,
            status=status,
            message=msg)
    else:
        return 'Rota apenas para requisições do tipo POST'