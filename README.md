# 🏠 House Price Prediction using Machine Learning

A Machine Learning web application that predicts house prices using a **Linear Regression** model. The project is developed with **Python, Scikit-learn, Flask, HTML, and CSS** and provides an easy-to-use web interface for predicting house prices based on user inputs.

---

## 📌 Project Overview

This project uses a **Linear Regression** algorithm to estimate house prices based on the following features:

- 💰 Average Area Income
- 🏡 Average Area House Age
- 🚪 Average Area Number of Rooms
- 🛏 Average Area Number of Bedrooms
- 👨‍👩‍👧 Area Population

The trained model is integrated with a **Flask web application**, allowing users to enter values through a browser and instantly receive a predicted house price.

---

## 🚀 Features

- ✅ Machine Learning based prediction
- ✅ Linear Regression model
- ✅ Interactive Flask Web Application
- ✅ Clean and Responsive User Interface
- ✅ Frontend Input Validation
- ✅ Backend Input Validation
- ✅ Error Handling
- ✅ Model saved using Pickle (.pkl)
- ✅ Easy to use and beginner-friendly

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Scikit-learn | Machine Learning Model |
| Flask | Backend Web Framework |
| HTML5 | Frontend Structure |
| CSS3 | User Interface Styling |
| Pickle | Saving Trained Model |
| Git & GitHub | Version Control |

---

## 📂 Project Structure

```text
House-Price-Prediction/
│
├── dataset/
│   └── housing.csv
│
├── model/
│   └── house_price_model.pkl
│
├── notebook/
│   └── house_price_prediction.ipynb
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Machine Learning Workflow

1. Import Libraries
2. Load Dataset
3. Data Exploration (EDA)
4. Data Preprocessing
5. Train-Test Split
6. Train Linear Regression Model
7. Evaluate Model
8. Save Model using Pickle
9. Build Flask Web Application
10. Predict House Price

---

## 📈 Model Performance

| Metric | Value |
|---------|-------|
| MAE | 80,879 |
| RMSE | 100,444 |
| R² Score | 0.918 |

The model achieves approximately **91.8% accuracy (R² Score)** on the test dataset.

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/kaushalkumar1006/House-Price-Prediction.git
```

Move into the project folder:

```bash
cd House-Price-Prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 📝 Input Parameters

| Parameter | Example |
|-----------|---------|
| Avg. Area Income | 65000 |
| Avg. Area House Age | 6 |
| Avg. Area Number of Rooms | 7 |
| Avg. Area Number of Bedrooms | 3 |
| Area Population | 35000 |

---

## 🔮 Future Improvements

- Add Multiple Machine Learning Models
- Compare Model Performance
- Deploy on Cloud (Render)
- Improve User Interface
- Add Data Visualization Dashboard
- Use Real Estate APIs

---

## 👨‍💻 Developer

**Kaushal Kumar**

Machine Learning & Python Developer

GitHub:
https://github.com/kaushalkumar1006

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

---

## 📜 License

This project is created for **educational and learning purposes**.