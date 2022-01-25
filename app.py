from flask import Flask, render_template

@app.route("/")
@app.route("/printMessage")
def printMessage():
  text = "**Message from app.py**"
  return render_template('index.html',message=text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
