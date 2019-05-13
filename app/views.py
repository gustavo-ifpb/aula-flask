from flask import render_template, request, redirect, url_for

from app import app

posts = []

@app.route('/', methods=['GET'])
def index():
    return render_template('twitter.html', posts=posts)

@app.route('/twitter', methods=['POST'])
def twitter():
    if request.method == 'POST':
        post = {}
        post['name'] = request.form['name']
        post['msg'] = request.form['msg']
        posts.append(post)
    return redirect(url_for('index'))