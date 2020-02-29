import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """"Main page with instructions"""
    return 'To send a message use /USERNAME/MESSAGE'

@app.route('/<username>')
def user(username):
    return 'Hi '+ username

@app.route('/<username>/<message>')
def send_message(username, message):
    return '{}: {}'.format(username, message)

app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
