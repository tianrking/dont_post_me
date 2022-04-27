from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello Medium"

@app.route("/who")
def who_am_i():
    return "w0x7ce"

if __name__ == '__main__':
    app.run(port=5000)
