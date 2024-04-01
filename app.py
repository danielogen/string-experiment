from flask import Flask, redirect, url_for, render_template,session, jsonify, request
from datetime import datetime
import randomize
import csv
import os

app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("consent.html")
@app.route("/declined")
def decline():
    return render_template("decline.html")

@app.route("/")
def home():
    # make sure session is empty at the start of each experience or
    # at the end of experience
    session.clear()
    return render_template("protocol.html")
# @app.route("/protocol")
# def protocol():
#     return render_template("protocol.html")
@app.route("/demographics")
def demographics():
    return render_template("demographics.html")

@app.route("/pre-tasks")
def pre_tasks():
    return render_template("pre-tasks.html")

@app.route("/experiment")
def experiment():
    # concatenation  = randomize.error_concatenation();
    return render_template("experiment.html")

@app.route("/process", methods=['POST'])
def process_demographics():
    session['age'] = request.form['age']
    session['COY'] = request.form['COY'] # college year
    session['YOE'] = request.form['YOE'] # year of programming experience
    session['gender'] = request.form['gender']
    return redirect(url_for('pre_tasks'))

@app.route('/save', methods=['POST'])
def save():
    data = request.get_json()
    # Data format: { questionId: { userAnswer: "X", correctAnswer: "Y" }, ... }

   # Format the filename with the current datetime to ensure uniqueness
    filename = f'reponses.csv'
    file_exists = os.path.exists(filename)
    
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        # CAT - Category, CA = Correct Answer, UA = User Answer
        if not file_exists:
            writer.writerow(['Gender', 'Age', 'COY', 'YOE', 'TaskID', 'CAT', 'CA', 'UA', 'Duration'])
        
        # Write the data rows
        for question_id, answers in data.items():
            writer.writerow([
                session['gender'],
                session['age'],
                session['COY'],
                session['YOE'],
                question_id,
                answers['category'],
                answers['correctAnswer'],
                answers['userAnswer'], 
                answers['duration']
            ])

    return jsonify({'status': 'success'})

if __name__ == "__main__":
    app.secret_key="v_qf*A&Juo)~9'D"
    app.run(debug=True)
