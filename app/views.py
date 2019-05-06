from app import app

@app.route('/')
def hello():
    return 'hello world!'

@app.route('/isaque')
def isaque():
    return 'Valeu isaque'