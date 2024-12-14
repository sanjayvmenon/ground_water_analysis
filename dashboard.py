from flask import Flask
from flask import render_template
from flask import request
from joblib import load
import pandas as pd
model = load('decision_tree_model.joblib')

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form submission
    try:
        TDS = float(request.form['TDS'])
        pH = float(request.form['pH'])
        WaterHardness = float(request.form['WaterHardness'])

        # Create input DataFrame
        input_data = pd.DataFrame([{
            'TDS': TDS,
            'pH': pH,
            'Water Hardness Score': WaterHardness
        }])

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Return the result
        return render_template('result.html', prediction=prediction)
    except Exception as e:
        return f"Error: {e}"


if __name__ == '__main__':
    app.run(debug=True)


