# 💧 Water Potability Prediction

A Machine Learning web application built with **Python and Streamlit** that predicts whether water is **potable (safe to drink)** or **not potable** based on different water quality parameters.

## 🚀 Live Demo

The application is deployed using **Streamlit Community Cloud**.

👉 **Live App:** Add your Streamlit URL here

## 📌 About the Project

This project uses a **Random Forest Classifier** to predict water potability.

The user enters different water-quality measurements into the Streamlit application, and the trained Machine Learning model predicts whether the water is potable or not.

## 📊 Input Features

The model uses the following parameters:

* pH
* Hardness
* Solids
* Chloramines
* Sulfate
* Conductivity
* Organic Carbon
* Trihalomethanes
* Turbidity

## 🤖 Machine Learning Model

* **Algorithm:** Random Forest Classifier
* **Problem Type:** Binary Classification
* **Target:** Potability

  * `0` → Not Potable
  * `1` → Potable

The trained model is saved using **Joblib** and loaded by the Streamlit application.

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Imbalanced-learn
* Joblib
* Streamlit

## 📁 Project Structure

```text
water-potability-app/
│
├── app.py
├── water_potability_model.pkl
├── requirements.txt
└── README.md
```

## ▶️ Run Locally

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Go to the project folder:

```bash
cd water-potability-app
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## Find the App here
https://check-water-potablility.streamlit.app/
## ⚠️ Disclaimer

This application is developed for **educational and demonstration purposes**. The prediction should not be considered a substitute for professional or certified water-quality testing.

## 👨‍💻 Author

**Qadees**

Machine Learning & Streamlit Project
