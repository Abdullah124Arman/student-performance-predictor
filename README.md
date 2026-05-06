# Student Performance Predictor 🎓

A machine learning application that predicts whether a student will **Pass or Fail** based on academic inputs — with a Python/Flask backend and a native Android frontend.

---

## 📱 App Demo

| Input Screen | Result Screen |
|---|---|
| Enter attendance, internal marks, assignment | Displays Pass/Fail with confidence % and risk level |

---

## 🚀 Features

- Predicts student academic outcome (Pass/Fail) in real time
- Shows prediction confidence percentage and risk level
- Native Android app connected to a Flask REST API
- Logistic Regression model trained on real UCI student dataset
- Handles missing input validation and error responses

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Machine Learning | Python, Scikit-learn, Logistic Regression |
| Data Processing | Pandas, NumPy |
| Backend API | Flask, OkHttp |
| Android App | Java, Android Studio |
| Model Persistence | Joblib (.pkl) |
| Dataset | UCI Student Performance Dataset |

---

## 📊 Model Performance

| Metric | Value |
|---|---|
| Algorithm | Logistic Regression |
| Accuracy | **89.07%** |
| Precision (Pass) | 91% |
| Precision (Fail) | 87% |
| Dataset size | 395 students |
| Train/Test Split | 70% / 30% |

> **Note:** Initial model showed 100% accuracy due to data leakage (G3 was used as both a feature and label). This was identified and fixed by removing G3 from input features and replacing assignment scores with studytime mapping.

---

## 🏗️ Project Architecture

```
UCI Dataset (student-mat.csv)
        ↓
prepare_dataset.py        → Cleans and transforms raw data
        ↓
student_dataset_real.csv  → Processed dataset
        ↓
train_from_csv.py         → Trains Logistic Regression model
        ↓
student_performance_model.pkl  → Saved trained model
        ↓
app.py (Flask API)        → Serves predictions via REST API
        ↓
Android App               → User interface for input/output
```

---

## 📂 Project Structure

```
student-performance-predictor/
│
├── app.py                      # Flask REST API
├── train_from_csv.py           # Model training script
├── prepare_dataset.py          # Data preprocessing
├── predict_from_model.py       # Standalone prediction script
├── student_performance_model.pkl  # Trained ML model
├── student_dataset_real.csv    # Processed dataset
├── student-mat.csv             # Original UCI dataset
├── test_api.py                 # API testing script
└── android/                    # Android Studio project
```

---

## ⚙️ How to Run Locally

### Backend (Flask API)

```bash
# Clone the repository
git clone https://github.com/Abdullah124Arman/student-performance-predictor.git
cd student-performance-predictor

# Install dependencies
pip install flask scikit-learn pandas numpy joblib

# Run the API
python app.py
```

API will start at `http://localhost:5000`

## 🌐 Live Deployment
The API is live and publicly accessible at:
**https://student-performance-predictor-op84.onrender.com**

### Test the API

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"attendance": 85, "internal1": 14, "internal2": 16, "assignment": 15}'
```

**Response:**
```json
{
  "prediction": "Pass",
  "confidence": "94.5%",
  "raw_value": 1
}
```

### Android App

1. Open the `android/` folder in Android Studio
2. Update the `PREDICT_URL` in `MainActivity.java` to your Flask server IP
3. Run on emulator or physical device

---

## 📥 Input Parameters

| Parameter | Description | Range |
|---|---|---|
| attendance | Student attendance percentage | 0 – 100 |
| internal1 | First internal exam marks | 0 – 20 |
| internal2 | Second internal exam marks | 0 – 20 |
| assignment | Assignment score | 0 – 20 |

---

## 👨‍💻 Author

**Abdullah Arman**  
B.Tech Computer Science & Engineering  
Parul University  
[GitHub](https://github.com/Abdullah124Arman) • [LinkedIn](https://www.linkedin.com/in/abdullah-arman-755a123b3/)

---

## 📄 Dataset Credit

[UCI Machine Learning Repository — Student Performance Dataset](https://archive.ics.uci.edu/ml/datasets/student+performance)
