from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def show_links():
    return """
    <h1>PAGE</h1>
        <ul>
            <li><a href="/welcome">Welcome!</a></li>
            <li><a href="/welcome/home">Welcome Home!</a></li>
            <li><a href="/welcome/back">Welcome Back!</a></li>
        </ul>
    """

@app.route('/welcome')
def welcome_user():
    return "<h1>welcome</h1>"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    return "welcome back"