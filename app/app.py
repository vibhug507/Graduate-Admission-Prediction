from flask import Flask,render_template,request
import numpy as np
from joblib import load

model = load('model.joblib')

app = Flask(__name__)

@app.route("/",methods = ['GET','POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        cgpa = float(request.form['CGPA'])
        toeflScore = float(request.form['TOEFL Score'])
        greScore = float(request.form['GRE Score'])
        universityRating = float(request.form['University Rating'])
        sop = float(request.form['SOP'])
        lor = float(request.form['LOR'])
        research = float(request.form['Research'])
        chanceOfAdmit = model.predict([[universityRating,sop,lor,cgpa,research]])
        if chanceOfAdmit[0] < 0.0:
            return ("Sorry, but your chances of admission are very low.\n")
        elif chanceOfAdmit > 1.0:
            return ("You might have entered incorrect data.\n")
        else:
            return ("Your chances of admission are " + str(chanceOfAdmit[0]) + ".\n")
