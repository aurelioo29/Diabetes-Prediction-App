from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/diabetes_prediction'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class DiabetesData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    no_hp = db.Column(db.String(15))
    pregnancies = db.Column(db.Integer)
    glucose = db.Column(db.Float)
    bloodpressure = db.Column(db.Float)
    skinthickness = db.Column(db.Float)
    insulin = db.Column(db.Float)
    bmi = db.Column(db.Float)
    diabetespedigree = db.Column(db.Float)
    age = db.Column(db.Integer)
    prediction_result = db.Column(db.String(50))

model = 'model/logistic_regression_diabetes_model.pkl'
with open(model, 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            name = request.form['name']
            no_hp = request.form['no_hp']
            pregnancies = int(request.form['pregnancies'])
            glucose = int(request.form['glucose'])
            bloodpressure = int(request.form['bloodpressure'])
            skinthickness = int(request.form['skinthickness'])
            insulin = int(request.form['insulin'])
            bmi = float(request.form['bmi'])
            diabetespedigree = float(request.form['diabetespedigree'])
            age = int(request.form['age'])

            features = [pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age]
            prediction = model.predict([features])
            output = "DIABETES" if prediction[0] == 1 else "TIDAK DIABETES"

            new_data = DiabetesData(
                name=name,
                no_hp=no_hp,
                pregnancies=pregnancies,
                glucose=glucose,
                bloodpressure=bloodpressure,
                skinthickness=skinthickness,
                insulin=insulin,
                bmi=bmi,
                diabetespedigree=diabetespedigree,
                age=age,
                prediction_result=output
            )

            db.session.add(new_data)
            db.session.commit()

            return jsonify({
                "prediction_text": output,
                "input_data": {
                    "Pregnancies": pregnancies,
                    "Glucose": glucose,
                    "Blood Pressure": bloodpressure,
                    "Skin Thickness": skinthickness,
                    "Insulin": insulin,
                    "BMI": bmi,
                    "Diabetes Pedigree": diabetespedigree,
                    "Age": age
                }
            })

        except Exception as e:
            print(f"Error occurred: {e}")
            return jsonify({
                "prediction_text": "Error: Mohon masukkan data yang valid atau periksa input Anda.",
                "input_data": {}
            })

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
