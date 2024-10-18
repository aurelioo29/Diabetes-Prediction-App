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
  features = [
    float(request.form['pregnancies']),
    float(request.form['glucose']),
    float(request.form['bloodpressure']),
    float(request.form['skinthickness']),
    float(request.form['insulin']),
    float(request.form['bmi']),
    float(request.form['diabetespedigree']),
    float(request.form['age']),
  ]

  feature_array = np.array(features).reshape(1, -1)

  prediction = model.predict(feature_array)

  output = "Diabetes" if prediction[0] == 1 else "Tidak Diabetes"
  return render_template('index.html', prediction_text='Hasil Prediksi: {}'.format(output))

if __name__ == '__main__':
  app.run(debug=True)