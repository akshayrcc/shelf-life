from flask import Flask, redirect, url_for, render_template, request, make_response

app = Flask(__name__)


# @app.route("/")
# def home():
#     return "This is the home page <h1> You are Welcome! </h1>"

# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}!"


# @app.route("/admin")
# def admin():
#     # return redirect(url_for("home"))
#     return redirect(url_for("user", name="Bob_admin"))

# @app.route("/<name>")
# def webpage(name):
#     # return redirect(url_for("home"))
#     return render_template("index.html", content=name)
@app.route('/')
def index():
    return render_template('cookies.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readcookies.html'))
        resp.set_cookie('userID', user)
        return resp


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    print(name)
    return '<h1>welcome ' + name + '</h1>'


if __name__ == "__main__":
    app.run(port=5500, debug=True)
