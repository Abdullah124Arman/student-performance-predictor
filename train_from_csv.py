# Author: Abdullah Arman
# Project: Student Performance Predictor
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# 1. Load the dataset from CSV
df = pd.read_csv("student_dataset_real.csv")
print("Dataset preview:")
print(df.head())

# 2. Separate input (X) and output (y)
X = df[["attendance", "internal1", "internal2", "assignment"]]
y = df["final_result"]

# 3. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 4. Create and train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# 4.5 Save the trained model to a file
joblib.dump(model, "student_performance_model.pkl")
print("\nModel saved as student_performance_model.pkl")

# 5. Test the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\nModel accuracy on test data:", accuracy)
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 6. Try predicting for a new student
new_student = pd.DataFrame(
    [[75, 20, 19, 8]],  # [attendance, internal1, internal2, assignment]
    columns=["attendance", "internal1", "internal2", "assignment"]
)

prediction = model.predict(new_student)
print("\nPrediction for new student (1 = Pass, 0 = Fail):", prediction[0])
