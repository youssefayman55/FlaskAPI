# 🌐 Emotion Classification API using Flask & Machine Learning

## 🧠 Overview

This project is a **REST API built with Flask** that serves a trained Machine Learning model for **emotion classification**.

The model predicts human emotions based on input features such as:

* Heart Rate ❤️
* Age 🎂

The API receives JSON data, processes it, and returns predicted emotions.

---

## 🚀 Features

* 🌐 REST API using Flask
* 🤖 Machine Learning model integration (joblib)
* 📊 Batch prediction support (multiple inputs)
* ⚡ Fast inference using NumPy
* 📩 JSON request/response format

---

## 🧠 Emotion Classes

The model predicts one of the following emotions:

* 😡 Angry
* 😨 Fear
* 😊 Happy
* 😐 Normal
* 😢 Sad

---

## 🛠️ Technologies Used

* Python 🐍
* Flask (Web Framework)
* Scikit-learn (ML Model)
* Joblib (Model Serialization)
* NumPy (Data Processing)

---

## 📂 Project Structure

```id="c2m8qp"
├── app.py
├── Machine_Learning_Model.pkl
└── README.md
```

---

## ▶️ How to Run

### 1. Install Dependencies

```bash id="m7x3vn"
pip install flask joblib numpy scikit-learn
```

### 2. Run the API

```bash id="k4p9qd"
python app.py
```

---

## 📡 API Endpoint

### 🔹 POST `/`

Send JSON data to get emotion predictions.

---

## 📥 Request Example

```json id="v3q8lm"
[
  {
    "Heart Rate": 85,
    "Age": 25
  },
  {
    "Heart Rate": 120,
    "Age": 40
  }
]
```

---

## 📤 Response Example

```json id="r8t2wx"
[
  { "Emotion": "Happy" },
  { "Emotion": "Fear" }
]
```

---

## 🎯 How It Works

* The API receives JSON input
* Extracts features (Heart Rate, Age)
* Converts them into NumPy array
* Loads the trained ML model
* Performs prediction
* Maps numerical output to emotion labels
* Returns JSON response

---

## 💡 Use Cases

* Emotion detection systems 🧠
* Healthcare monitoring ❤️
* Smart wearable analytics ⌚
* Behavioral analysis systems 📊

---

## 💡 Future Improvements

* Add authentication (API security) 🔐
* Deploy using Docker 🐳
* Host on cloud (AWS / Render / Heroku) ☁️
* Add real-time streaming input
* Expand model with more physiological features

---

## ⚠️ Notes

* Ensure `Machine_Learning_Model.pkl` exists in the correct path
* API currently supports POST requests only
* Input must be valid JSON format

---

## 👨‍💻 Author

**Youssef Ayman**
AI Engineer & Data Scientist

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
