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

## 📊 Model Performance: Live Match Validation

A true test of any predictive model lies in its real-world performance, especially for dynamic events like a cricket match. For win probability, **probability calibration** – how closely the predicted probabilities align with actual observed frequencies – is often more crucial than simple classification accuracy.

To validate my model's capabilities, I tracked a live cricket match (Mumbai Indians vs. Royal Challengers Bangalore, for example) and compared its real-time win probability predictions against those displayed on the highly reputable **ESPN Cricinfo** website.

### **Visualizing Live Probability Shifts**

The plot below illustrates how both my model's and Cricinfo's predicted win probabilities for the **Bowling Team** evolved over the course of the match. Key events that influenced momentum are also highlighted, providing essential context to the probability swings.

![Win Probability Comparison Plot](win_probability_comparison.png)
