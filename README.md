# 🏏 T20 Cricket Match Win Probability Predictor

This project develops a machine learning model to predict **real-time win probabilities** for cricket matches during second innings chases. Beyond just predicting the final outcome, this model aims to provide dynamic insights into how match conditions – such as runs scored, wickets fallen, and overs played and others – influence the likelihood of victory.

---

## 🎯 Project Goal

The primary objective is to build a robust and intuitive win probability predictor that can be validated against established real-world benchmarks, demonstrating an end-to-end data science workflow from model development to interactive deployment.

---

## ✨ Features & Technologies

* **Real-time Probability Prediction:** Dynamic updates to win probabilities as the match progresses.
* **Comprehensive Feature Engineering:** Utilizes key in-match statistics like runs scored, wickets taken, and overs completed.
* **Robust Preprocessing Pipeline:** Employs `scikit-learn`'s `ColumnTransformer` and `OneHotEncoder` for handling categorical features, ensuring consistency between training and deployment.
* **Model Validation:** Comparative analysis against professional benchmarks (e.g., ESPN Cricinfo).
* **Interactive Web Application:** Built with `Streamlit` for an accessible user interface.
* **Deployment Ready:** Model saved using `joblib` for seamless integration into web services.

**Technologies Used:**

* **Python**
* **Pandas** (Data Manipulation)
* **NumPy** (Numerical Operations)
* **Scikit-learn** (Machine Learning Model & Preprocessing)
* **Joblib** (Model Serialization)
* **Streamlit** (Web Application Framework)
* **Matplotlib & Seaborn** (Data Visualization)

---
