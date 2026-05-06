from sklearn.linear_model import LogisticRegression
import numpy as np

# ===== 1. Create a tiny fake dataset =====
# Each row: [attendance_percentage, internal_marks]
X = np.array([
    [90, 24],
    [85, 22],
    [70, 18],
    [60, 15],
    [50, 12],
    [40, 10],
])

# Final result: 1 = Pass, 0 = Fail
y = np.array([1, 1, 1, 0, 0, 0])

# ===== 2. Create and train the model =====
model = LogisticRegression()
model.fit(X, y)

# ===== 3. Test the model with a new student's data =====
# Example student: 75% attendance, 20 internal marks
new_student = np.array([[75, 20]])
prediction = model.predict(new_student)
probability = model.predict_proba(new_student)

print("Prediction (1 = Pass, 0 = Fail):", prediction[0])
print("Probabilities [Fail, Pass]:", probability[0])
