# Author: Abdullah Arman
# Project: Student Performance Predictor
from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Create Flask app
app = Flask(__name__)

# Load the trained model once when the app starts
model = joblib.load("student_performance_model.pkl")
print("Model loaded successfully in API.")

@app.route("/")
def home():
    return "Student Performance Prediction API is running."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Required fields
        required_fields = ["attendance", "internal1", "internal2", "assignment"]

        # Check if all required fields are present
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Extract values and convert to float
        attendance = float(data["attendance"])
        internal1 = float(data["internal1"])
        internal2 = float(data["internal2"])
        assignment = float(data["assignment"])

        # Create DataFrame in the same format as training
        new_student = pd.DataFrame(
            [[attendance, internal1, internal2, assignment]],
            columns=["attendance", "internal1", "internal2", "assignment"]
        )

        # Make prediction
        pred = model.predict(new_student)[0]

        # Get prediction probability
        prob = model.predict_proba(new_student)[0]
        confidence = round(max(prob) * 100, 2)

        label = "Pass" if pred == 1 else "Fail"

        # Return result
        return jsonify({
            "prediction": label,
            "confidence": f"{confidence}%",
            "raw_value": int(pred)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)