from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello!! this is main page</h1>"

@app.route("/<name>")
def user(name):
    return f"<h1>hello {name}<h1>"

if __name__ == "__main__":
    app.run()