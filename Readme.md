# 🎓 Student Performance Predictor

## 📌 Project Overview

This project is a Machine Learning based web application built using Streamlit. It predicts student performance based on academic inputs like study hours, attendance, and assignments.

The system also classifies whether a student will PASS or FAIL.

---

## 🚀 Features

- Interactive web interface using Streamlit
- Predicts student marks using Linear Regression
- Classifies PASS or FAIL using Decision Tree Classifier
- Real-time prediction system
- Simple slider-based input system

---

## 🧠 Machine Learning Models Used

### 1. Linear Regression
Used to predict expected student marks based on:
- Study Hours
- Attendance
- Assignments

### 2. Decision Tree Classifier
Used to predict final result (PASS/FAIL) based on:
- Study Hours
- Attendance
- Assignments
- Previous Marks (predicted by Linear Regression)

---

## 📊 Dataset

The dataset used in this project is synthetically generated using a custom Python script (`generate_dataset.py`).

It contains randomly generated values for:
- Study Hours
- Attendance
- Assignments
- Previous Marks
- Result (0 = Fail, 1 = Pass)

This dataset is created for learning and demonstration purposes only.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
## 🎓 Student Performance Predictor (Live App)

This project is deployed using Streamlit Cloud.

🌐 Live Demo: https://bvcbds3q9yzuhcuyeyrsab.streamlit.app/

👉 Open the link and try the interactive ML model.