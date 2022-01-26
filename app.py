#Ref: https://flask.palletsprojects.com/en/2.0.x/quickstart/
#Ref: https://hackersandslackers.com/flask-routes/
#Import the Flask class and related functions used in this app
from flask import Flask, redirect, url_for, render_template

#Create an instance of the Flask class and call it as the name 'app'
app = Flask(__name__)

#app.route("/") is call to the root URL and will execute the codes in the 'home' view function
@app.route("/")
def home():
  #Redirect(url_for ......) is to redirect the user to the path specified in this case /printMessage and pass the variable 'message' over
  return redirect(url_for('printMessage', message='Hello its me!!'))

#Call to the /printMessage URL and will execute the codes in the 'printMessage' view function which will accept an argument 'message'
@app.route("/printMessage/<message>")
def printMessage(message):
  #return render_template will call an HTML page to the user in this case 'index.html' which by default located in the 'templates' directory
  return render_template('index.html',message=message)
