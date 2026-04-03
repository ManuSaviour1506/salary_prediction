# 💼 Salary Prediction System (ML + Streamlit)
### 🚀 Overview

#### The Salary Prediction System is a Machine Learning web application that predicts a developer’s salary based on:

👨‍💻 Skills (Python, React, Java, etc.)
🌍 Country (India, USA, Germany, etc.)
📈 Experience
🏢 Company Size
🎓 Education Level

The model is built using Random Forest Regression and deployed with Streamlit for real-time predictions.

🖼️ EDA Preview
<p align="center">
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775204121/Screenshot_2026-04-03_at_1.36.55_PM_h4b5sf.png"width="45%" />
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775204121/Screenshot_2026-04-03_at_1.36.43_PM_q0aauo.png" width="45%" />
</p>
<p align="center">
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775204120/Screenshot_2026-04-03_at_1.37.11_PM_g6f0t6.png" width="45%" />
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775204120/Screenshot_2026-04-03_at_1.37.23_PM_o7hs77.png" width="45%" />
</p>


## 🧠 Machine Learning Details
### Algorithm: Random Forest Regressor
Libraries Used:
pandas
scikit-learn
joblib
## ⚙️ Workflow
Data Collection → Preprocessing → Feature Engineering → Model Training → Evaluation → Deployment
## 📊 Features
✅ Real-time salary prediction
✅ One-hot encoding for categorical features
✅ Handles multiple skills selection
✅ Model saved using joblib
## 🛠️ Tech Stack
Layer	Technology
Frontend	Streamlit
Backend	Python
ML Model	Random Forest Regression
Serialization	Joblib

## 📁 Project Structure
salary-predictor/
│
├── app.py                # Streamlit app
├── salary_model.pkl     # Trained ML model
├── columns.pkl          # Feature columns
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
## 🖥️ Streamlit UI Analysis
The application provides an interactive dashboard where users can input patient metrics. The model then processes these through a `StandardScaler` and a `Logistic Regression` classifier to provide a real-time diagnosis.

<p align="center">
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775204120/Screenshot_2026-04-03_at_1.35.26_PM_eefsby.png" width="80%">
  <br>
  <img src="https://res.cloudinary.com/ddgfjerss/image/upload/v1775204119/Screenshot_2026-04-03_at_1.34.52_PM_mcm8gv.png" width="80%">
</p>

## ⚡ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/ManuSaviour1506/salary_prediction.git
cd salary-predictor
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Application
streamlit run app.py
💡 Example Input
Experience: 3 years
Country: India
Skills: Python, Django
🎯 Output
Predicted Salary: $ 27,000
## 🔥 Key Highlights
📈 Predicts salary based on real-world factors
🧠 Uses ensemble learning (Random Forest)
⚡ Fast and lightweight deployment
💻 Beginner-to-intermediate ML project

<h2 align="center">👨‍💻 Manu Saviour</h2>

<p align="center">
  <b>Full Stack Developer • Machine Learning • DevOps • Data Science</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Full%20Stack-Developer-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Machine%20Learning-AI-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/DevOps-Engineer-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Data%20Science-Analytics-purple?style=for-the-badge" />
</p>

<p align="center">
  🚀 Building scalable web applications | 🤖 Exploring AI | ⚙️ Engineering systems
</p>
