from flask import Flask, request, jsonify, render_template
import pandas as pd
import os
from dotenv import load_dotenv
import json
import random

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
ENDPOINT = os.getenv("ENDPOINT")

app = Flask(__name__)

df = pd.read_csv("adult_income.csv")  # Example dataset for bias detection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Generate random prediction values
    prediction = {
        "bias_score": round(random.uniform(0, 1), 2),
        "fairness_status": random.choice(["Fair", "Slightly Biased", "Highly Biased"]),
        "accuracy": round(random.uniform(80, 100), 2),
        "precision": round(random.uniform(70, 95), 2),
        "recall": round(random.uniform(60, 90), 2)
    }
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True)