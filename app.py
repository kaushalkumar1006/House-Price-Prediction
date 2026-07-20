from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# ==========================
# Load Trained Model
# ==========================
with open("model/house_price_model.pkl", "rb") as file:
    model = pickle.load(file)


# ==========================
# Home Page
# ==========================
@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# Prediction Route
# ==========================
@app.route("/predict", methods=["POST"])
def predict():

    try:
        # --------------------------
        # Get Input Values
        # --------------------------
        income = float(request.form["income"])
        age = float(request.form["age"])
        rooms = float(request.form["rooms"])
        bedrooms = float(request.form["bedrooms"])
        population = float(request.form["population"])

        # --------------------------
        # Input Validation
        # --------------------------

        if not (10000 <= income <= 120000):
            return render_template(
                "index.html",
                prediction_text="❌ Avg. Area Income should be between 10,000 and 120,000."
            )

        if not (1 <= age <= 20):
            return render_template(
                "index.html",
                prediction_text="❌ Avg. Area House Age should be between 1 and 20 years."
            )

        if not (2 <= rooms <= 10):
            return render_template(
                "index.html",
                prediction_text="❌ Avg. Area Number of Rooms should be between 2 and 10."
            )

        if not (1 <= bedrooms <= 6):
            return render_template(
                "index.html",
                prediction_text="❌ Avg. Area Number of Bedrooms should be between 1 and 6."
            )

        if not (5000 <= population <= 100000):
            return render_template(
                "index.html",
                prediction_text="❌ Area Population should be between 5,000 and 100,000."
            )

        # --------------------------
        # Create DataFrame
        # --------------------------
        data = pd.DataFrame({
            "Avg. Area Income": [income],
            "Avg. Area House Age": [age],
            "Avg. Area Number of Rooms": [rooms],
            "Avg. Area Number of Bedrooms": [bedrooms],
            "Area Population": [population]
        })

        # --------------------------
        # Predict Price
        # --------------------------
        prediction = model.predict(data)[0]

        # Return Result
        return render_template(
            "index.html",
            prediction_text=f"Predicted House Price (USD): ${prediction:,.2f}"
        )

    except ValueError:
        return render_template(
            "index.html",
            prediction_text="❌ Please enter valid numeric values."
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"❌ Error: {str(e)}"
        )


# ==========================
# Run Flask App
# ==========================
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)