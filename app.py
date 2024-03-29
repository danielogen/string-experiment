from flask import Flask, redirect, url_for, render_template,session
import randomize
import random

app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("consent.html")
@app.route("/declined")
def decline():
    return render_template("decline.html")

@app.route("/")
def home():
    return render_template("protocol.html")

# @app.route("/protocol")
# def protocol():
#     return render_template("protocol.html")
@app.route("/pre-expriment")
def decline():
    return render_template("pre-expriment.html")

@app.route("/experiment")
def experiment():
    concatenation  = randomize.error_concatenation();
    return render_template("experiment.html", concatenation=concatenation)

if __name__ == "__main__":
    app.secret_key="v_qf*A&Juo)~9'D"
    app.run(debug=True)
