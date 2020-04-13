from flask import render_template

from app import app,APP_ROOT

@app.route('/')
def home():
    return render_template('index.html',title='Home')

@app.route('/about')
def about():
    return render_template('about.html',title='About',name='Passed by variable')
