from flask import Flask

# export FLASK_APP=app  filename(app.py) flask run
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"