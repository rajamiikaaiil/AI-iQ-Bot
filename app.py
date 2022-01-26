#Ref: https://flask.palletsprojects.com/en/2.0.x/quickstart/
#Ref: https://hackersandslackers.com/flask-routes/
#Import the Flask class and related functions used in this app
from flask import Flask, redirect, url_for, render_template

#Create an instance of the Flask class and call it as the name 'app'
app = Flask(__name__)

#app.route("/") is call to the root URL
#Combine both / and /printMessage URLs to handle multiple routes with a single function ie printMe()
@app.route("/")
def home():
  return redirect(url_for('printMessage', message='Hello its me!!'))

@app.route("/printMessage/<message>")
def printMessage(message):
  return render_template('index.html',message=message)
