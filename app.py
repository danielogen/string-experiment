from flask import Flask, redirect, url_for, render_template,session, jsonify, request,send_file
from datetime import datetime
import randomize
import csv
import os
import uuid
import pandas as pd
import boto3
from boto3.s3.transfer import S3Transfer
from dotenv import load_dotenv
load_dotenv()

s3_client = boto3.client('s3', aws_access_key_id=os.environ['AccessKey'], aws_secret_access_key=os.environ['SecreteAccessKey'])
transfer = S3Transfer(s3_client)

app = Flask(__name__)
app.secret_key="v_qf*A&Juo)~9'D"

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
    session['uid'] = str(uuid.uuid1())[:8]
    return redirect(url_for('pre_tasks'))

@app.route('/save', methods=['POST'])
def save():
    data = request.get_json()
    
    data_for_df = [
    {
        'UID': session['uid'],
        'Gender': session['gender'],
        'Age': session['age'],
        'COY': session['COY'],
        'YOE': session['YOE'],
        'TaskID': question_id,
        'Complexity': answers['complexity'],
        'CAT': answers['category'],
        'CA': answers['correctAnswer'],
        'UA': answers['userAnswer'],
        'Duration': answers['duration']
    }
    for question_id, answers in data.items()
    ]

    # Create DataFrame
    df = pd.DataFrame(data_for_df)
    # df.to_csv(f"data/responses.csv")
    df.to_csv(f"/tmp/{session['uid']}_response.csv")
    transfer.upload_file(f"/tmp/{session['uid']}_response.csv", "string-experiment", os.environ['AccessKey'], extra_args={'ServerSideEncryption': "AES256"})

    return jsonify({'status': 'success'})

@app.route("/responses")
def responses():
    return render_template("responses.html")

@app.route('/download')
def download():
    path = f"/tmp/{session['uid']}_response.csv"
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
