# Author: Abdullah Arman
# Project: Student Performance Predictor
import pandas as pd

df = pd.read_csv("student-mat.csv", sep=";")

# Attendance approximation
df["attendance"] = (100 - (df["absences"] * 2)).clip(0, 100)

# Internal marks
df["internal1"] = df["G1"]
df["internal2"] = df["G2"]

# Assignment from studytime (1-4 scale, mapped to 0-20)
df["assignment"] = df["studytime"] * 5

# G3 removed from features to avoid data leakage
# final_result is derived from G3 but G3 itself is not used as input
df["final_result"] = df["G3"].apply(lambda x: 1 if x >= 10 else 0)

new_df = df[["attendance", "internal1", "internal2", "assignment", "final_result"]]
new_df.to_csv("student_dataset_real.csv", index=False)

print("Dataset prepared!")
print(new_df.head())
print(f"Total rows: {len(new_df)}")
print(f"Pass: {new_df['final_result'].sum()}, Fail: {new_df['final_result'].sum() - len(new_df)}")