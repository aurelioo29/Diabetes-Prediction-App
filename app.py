from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = 'model/logistic_regression_diabetes_model.pkl'
with open(model, 'rb') as file:
  model = pickle.load(file)

@app.route('/')
def home():
  return render_template('index.html');

@app.route('/predict', methods=['POST'])
def predict():
  try:
      # Ambil data dari form input
      pregnancies = request.form['pregnancies']
      glucose = request.form['glucose']
      bloodpressure = request.form['bloodpressure']
      skinthickness = request.form['skinthickness']
      insulin = request.form['insulin']
      bmi = request.form['bmi']
      diabetespedigree = request.form['diabetespedigree']
      age = request.form['age']
      
      if not all([pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigree, age]):
        return render_template('index.html', prediction_text="Mohon lengkapi semua field!")

      # Konversi input menjadi array numpy
      features = [float(pregnancies), float(glucose), float(bloodpressure), float(skinthickness), float(insulin), float(bmi), float(diabetespedigree), float(age)]
      prediction = model.predict([features])

      output = "Diabetes" if prediction[0] == 1 else "Tidak Diabetes"

      # Kirim data input dan hasil prediksi kembali ke template
      return render_template('index.html', 
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
    return render_template('index.html', prediction_text="Error: Mohon masukkan data yang valid!")

if __name__ == '__main__':
  app.run(debug=True)