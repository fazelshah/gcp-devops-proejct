from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Simple Flask application hosted on GKE using devops best practice!!!!!!!!!!!!'
