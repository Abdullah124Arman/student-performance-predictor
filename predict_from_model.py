# Author: Abdullah Arman
# Project: Student Performance Predictor
import joblib
import pandas as pd

# 1. Load the saved model from the .pkl file
model = joblib.load("student_performance_model.pkl")
print("Model loaded successfully.")

# 2. Take input from the user
print("\nEnter student details below:")

attendance = float(input("Attendance (%): "))
internal1 = float(input("Internal 1 marks: "))
internal2 = float(input("Internal 2 marks: "))
assignment = float(input("Assignment marks: "))

# 3. Prepare the data in correct format
new_student = pd.DataFrame(
    [[attendance, internal1, internal2, assignment]],
    columns=["attendance", "internal1", "internal2", "assignment"]
)

# 4. Predict using the loaded model
prediction = model.predict(new_student)[0]
prediction_label = "Pass" if prediction == 1 else "Fail"

# 5. Show results
print("\n=== Student Input Data ===")
print(new_student)

print("\n=== Prediction Result ===")
print(f"Prediction: {prediction_label} (raw value = {prediction})")

