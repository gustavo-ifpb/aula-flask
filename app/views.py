import psycopg2, psycopg2.extras

from flask import g, render_template, request, redirect, url_for, session

from app import app

# ~~~~
@app.before_request
def before_request():
    g.db = psycopg2.connect('dbname=twitter user=guga password=gugasv host=127.0.0.1')

@app.teardown_request
def teardown_request(exception):
    g.db.close()
# ~~~~


@app.route('/', methods=['GET'])
def index():
    session_name = ''
    if 'name' in session:
        session_name = session['name']

    cur = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    q = None
    if 'query' in request.args:
        q = request.args['query']
        cur.execute(f"SELECT * FROM post WHERE name ILIKE '{request.args['query']}'")
    else:
        cur.execute('SELECT * FROM post')
    posts = cur.fetchall()
    cur.close()
    
    return render_template('twitter.html', posts=posts, session_name=session_name, query=q)

@app.route('/search/<text>', methods=['GET'])
def search(text):
    session_name = ''
    if 'name' in session:
        session_name = session['name']

    cur = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(f"SELECT * FROM post WHERE name ILIKE '{text}'")
    posts = cur.fetchall()
    cur.close()
    
    return render_template('twitter.html', posts=posts, session_name=session_name, query=text)

@app.route('/twitter', methods=['POST'])
def twitter():
    if request.method == 'POST':

        cur = g.db.cursor()
        cur.execute(f"INSERT INTO post (name, tweet) VALUES ('{request.form['name']}', '{request.form['msg']}')")
        g.db.commit()
        cur.close()

        session['name'] = request.form['name']
    return redirect(url_for('index'))