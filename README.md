# ☀️ SolarOptima: Non-Linear Power Predictor

SolarOptima is a machine learning application designed to predict the DC power output of solar plants. Unlike standard linear models, this project utilizes **Polynomial Regression** to account for the non-linear relationship between panel temperature and energy efficiency.

## 🚀 The Problem

Solar panel efficiency doesn't follow a straight line. While more sunlight (Irradiation) increases power, rising **Module Temperature** eventually causes a drop in efficiency. Simple linear regression fails to capture this "plateau" and "dip," leading to inaccurate energy forecasts.

## 🧠 The Solution: Polynomial Regression

By transforming our input features into **2nd-degree polynomials**, the model can learn the parabolic relationship between temperature, time of day, and energy yield.

* **Algorithm:** Linear Regression with Polynomial Feature Transformation.
* **Accuracy ():** 0.9821
* **Key Insights:** The model successfully identifies "Thermal Throttling" where panels lose efficiency at high heat.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Data Science:** Pandas, NumPy, Scikit-Learn
* **Serialization:** Pickle (for model deployment)
* **Frontend:** Streamlit (Interactive Dashboard)

## 📊 Dataset

The model was trained on the **[Solar Power Generation Data](https://www.kaggle.com/datasets/anikannal/solar-power-generation-data)** from Kaggle.

* **Independent Features:** Irradiation, Ambient Temperature, Module Temperature, Hour of Day.
* **Target Variable:** DC Power Output (kW).

## 💻 How to Run

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/solar-optima.git
cd solar-optima

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the Streamlit App:**
```bash
streamlit run app.py

```



## 📈 Features

* **Real-time Prediction:** Adjust weather sliders to see instantaneous power forecasts.
* **Non-Linear Analysis:** Interactive charts showing how power output curves as temperature increases.
* **Contextual UI:** Visual feedback on whether the current conditions represent Peak or Low production hours.

---

### `requirements.txt`

`requirements.txt`

```text
streamlit
pandas
numpy
scikit-learn
plotly

```
