from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/healthcheck")
def healthcheck():
    return "I am alive!"


if __name__ == "__main__":
    app.run()
