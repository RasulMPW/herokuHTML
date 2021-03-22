
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():

    return render_template('welcome.html')
@app.route('/first')
def first():
    return render_template('first.html')
@app.route('/home')#
def login():
    return render_template('login.html')

