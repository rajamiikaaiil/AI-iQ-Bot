from flask import render_template

#@app.route('/')
@app.route('/printMessage')
def printMessage():
  text = '**Message from app.py**'
  return render_template('index.html',message=text)
