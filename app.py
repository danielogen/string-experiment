from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("consent.html")

@app.route("/")
def home():
    return render_template("protocol.html")

@app.route("/declined")
def decline():
    return render_template("decline.html")

# @app.route("/protocol")
# def protocol():
#     return render_template("protocol.html")

@app.route("/experiment")
def experiment():
    return render_template("experiment.html")

if __name__ == "__main__":
    app.run(debug=True)
