# Diabetes Prediction for Female Patients

## Overview

This project is a web application designed to predict diabetes in female patients using machine learning. The application allows users to input various health attributes and receive a prediction on whether the patient has diabetes.

## Setup and Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/aurelioo29/prediction-diabetes
   cd prediction-diabetes
   ```

2. **Create a virtual environment**:

   ```sh
   python -m venv env
   ```

   - On macOS/Linux:

   ```sh
   source env/bin/activate
   ```

   - On Windows:

   ```sh
   source env/bin/activate
   ```

   Activate environment:

   ```sh
   env\Scripts\activate
   ```

3. **Install the dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database**:

   - Ensure you have MySQL installed and running.
   - Create a database named `diabetes_prediction`.
   - Run the SQL and import our database `diabetes_prediction.sql`.

5. **Run the Flask application**:

   ```sh
   python app.py
   ```

6. **Access the application**:

   Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. Fill out the form with the required health attributes.
2. Click the "Prediksi" button to get the prediction.
3. The prediction result will be displayed along with the input data and classification report.

## Dependencies

- Flask
- Flask-SQLAlchemy
- MySQL-connector-python
- PyMySQL
- scikit-learn
- numpy
- scipy
- joblib

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.