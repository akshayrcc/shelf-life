from flask import Flask

app = Flask(__main__)

@app.route()
def home():
    return "This is the home page"

if __name__ == "__main__":
    app.run()