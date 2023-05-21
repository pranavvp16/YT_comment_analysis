from flask import Flask
from helper import sentiment
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def print():
    return "<h1>Yeah this works asf<h1>"

@app.route("analysis")
def analyse():
    return "<h1>This function analyses the video<h1>"







