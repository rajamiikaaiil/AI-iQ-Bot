#Ref: https://flask.palletsprojects.com/en/2.0.x/quickstart/
#Import the Flask class and related functions used in this app
from flask import Flask, render_template

#Create an instance of the Flask class and call it as the name 'app'
app = Flask(__name__)

#Combine both / and /printMessage URLs to handle multiple routes with a single function ie printMe()
@app.route("/")
@app.route("/printMessage")
def printMe():
  text = "**Message from app.py**"
  return render_template('index.html',message=text)

#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8080)
