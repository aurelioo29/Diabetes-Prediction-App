from flask import Flask, request, render_template
import pickle
import numpy as np
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12Axatower34@:3307/diabetes_prediction'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model database
class DiabetesData(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))  # Kolom untuk menyimpan nama
  no_hp = db.Column(db.String(15))  # Kolom untuk menyimpan nomor HP
  pregnancies = db.Column(db.Integer)
  glucose = db.Column(db.Float)
  bloodpressure = db.Column(db.Float)
  skinthickness = db.Column(db.Float)
  insulin = db.Column(db.Float)
  bmi = db.Column(db.Float)
  diabetespedigree = db.Column(db.Float)
  age = db.Column(db.Integer)
  prediction_result = db.Column(db.String(50)) 

# Muat model prediksi dari file pickle
model = 'model/logistic_regression_diabetes_model.pkl'
with open(model, 'rb') as file:
  model = pickle.load(file)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/prediction')
def prediction():
  return render_template('prediction.html')

@app.route('/predict', methods=['POST'])
def predict():
  try:
    name = request.form['name']  
    no_hp = request.form['no_hp']  
    pregnancies = int(request.form['pregnancies'])
    glucose = float(request.form['glucose'])
    bloodpressure = float(request.form['bloodpressure'])
    skinthickness = float(request.form['skinthickness'])
    insulin = float(request.form['insulin'])
    bmi = float(request.form['bmi'])
    diabetespedigree = float(request.form['diabetespedigree'])
    age = int(request.form['age'])

    # if not all([pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age]):
    #   return render_template('prediction.html', prediction_text="Mohon lengkapi semua field!")

    features = [pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age]
    prediction = model.predict([features])

    output = "Diabetes" if prediction[0] == 1 else "Tidak Diabetes"

        # Simpan data ke MySQL
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

        # Kirim data input dan hasil prediksi kembali ke template
    return render_template('prediction.html',
                          prediction_text=f"Hasil Prediksi: {output}",
                          input_data={
                              "Pregnancies": pregnancies,
                              "Glucose": glucose,
                              "Blood Pressure": bloodpressure,
                              "Skin Thickness": skinthickness,
                              "Insulin": insulin,
                              "BMI": bmi,
                              "Diabetes Pedigree": diabetespedigree,
                              "Age": age
                          })

  except Exception as e:
    print(f"Error occurred: {e}")
    return render_template('prediction.html', prediction_text="Error: Mohon masukkan data yang valid atau periksa input Anda.", input_data={})


if __name__ == '__main__':
  app.run(debug=True)