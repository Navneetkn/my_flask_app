from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv(".env")
version = os.environ.get("VERSION")

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Version = {}</p><h1>Hello!! this is main page</h1>".format(version)

@app.route("/<name>")
def user(name):
    return f"<h1>hello {name}<h1>"

if __name__ == "__main__":
    app.run()