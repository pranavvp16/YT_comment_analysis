from flask import Flask, render_template, request
from helper import sentiment
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
@app.route("/home",methods=['GET','POST'])
def print():
    return render_template('home.html')

@app.route("/analysis",methods=['POST'])
def analyse():
    video_url = request.form['video_url']

    return f"the entered video_url is {video_url}"







