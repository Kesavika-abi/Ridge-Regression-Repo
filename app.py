from flask import Flask, render_template, request
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model/model.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get values from form
        active_users = float(request.form["active_users"])
        ad_spend = float(request.form["ad_spend"])
        churn_rate = float(request.form["churn_rate"])
        in_app_revenue = float(request.form["in_app_revenue"])

        # Prepare input for model
        features = np.array([[active_users, ad_spend, churn_rate, in_app_revenue]])

        # Make prediction
        prediction = model.predict(features)[0]

        return render_template("result.html", revenue=round(prediction, 2))

    except Exception as e:
        return render_template("result.html", revenue=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
