from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "This is the home page <h1> You are Welcome! </h1>"


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


@app.route("/admin")
def admin():
    # return redirect(url_for("home"))
    return redirect(url_for("user", name="Admin!"))


if __name__ == "__main__":
    app.run(port=5500, debug=True)
