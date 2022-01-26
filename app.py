#Ref: https://flask.palletsprojects.com/en/2.0.x/quickstart/
#Import the Flask class and related functions used in this app
from flask import Flask, redirect, url_for, render_template

#Create an instance of the Flask class and call it as the name 'app'
app = Flask(__name__)

#app.route("/") is call to the root URL
#Combine both / and /printMessage URLs to handle multiple routes with a single function ie printMe()
@app.route("/")
def home():
  return redirect(url_for('printMessage', message='Hello it me!!'))

@app.route("/printMessage/<message>")
def printMe(message):
  #text = "**Message from app.py**"
  return render_template('index.html',message=message)

#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8080)
