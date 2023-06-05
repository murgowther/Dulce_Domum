from flask import render_template,redirect, url_for
from app import app

@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/logout')
def logout():
    return redirect(url_for('index'))
@app.route('/register')
def register():
    return render_template('register.html')
