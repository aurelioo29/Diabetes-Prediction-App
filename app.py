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

model_path = 'model/logistic_regression_diabetes_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            no_hp = request.form.get('no_hp')
            pregnancies = request.form.get('pregnancies')
            glucose = request.form.get('glucose')
            bloodpressure = request.form.get('bloodpressure')
            skinthickness = request.form.get('skinthickness')
            insulin = request.form.get('insulin')
            bmi = request.form.get('bmi')
            diabetespedigree = request.form.get('diabetespedigree')
            age = request.form.get('age')

            if not all([name, no_hp, pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age]):
                return jsonify({
                    "error": True,
                    "message": "Mohon lengkapi semua field!"
                }), 400

            pregnancies = int(pregnancies)
            glucose = int(glucose)
            bloodpressure = int(bloodpressure)
            skinthickness = int(skinthickness)
            insulin = int(insulin)
            bmi = float(bmi)
            diabetespedigree = float(diabetespedigree)
            age = int(age)

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
                "error": False,
                "prediction_text": output,
                "input_data": {
                    "Nama": name,
                    "Nomor HP": no_hp,
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
                "error": True,
                "message": "Harap masukkan data yang valid di setiap form.",
                "input_data": {}
            })

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
