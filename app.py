from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import json
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

app = Flask(__name__)

# Load trained ML model
model = joblib.load("model/solar_model.pkl")

# Load maintenance knowledge
with open("knowledge/maintenance.json", "r") as file:
    maintenance_data = json.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    input_data = pd.DataFrame({
        "temperature": [float(data["temperature"])],
        "humidity": [float(data["humidity"])],
        "irradiance": [float(data["irradiance"])],
        "cloud_cover": [float(data["cloud_cover"])],
        "wind_speed": [float(data["wind_speed"])],
        "panel_temperature": [float(data["panel_temperature"])]
    })

    prediction = model.predict(input_data)[0]

    return jsonify({
        "predicted_energy": round(float(prediction), 2)
    })


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    question = data.get("question", "").lower()

    if not question:
        return jsonify({
            "answer": "Please enter a maintenance question."
        })

    best_match = None

    # Search maintenance knowledge
    for item in maintenance_data.values():

        for keyword in item["keywords"]:

            if keyword in question:
                best_match = item
                break

        if best_match:
            break

    # Use general maintenance guidance if no specific match
    if best_match is None:
        best_match = maintenance_data["general"]

    response = best_match["title"] + "\n\n"

    for number, step in enumerate(best_match["steps"], start=1):
        response += f"{number}. {step}\n"

    return jsonify({
        "answer": response
    })
@app.route("/chart")
def chart():

    data = pd.read_csv("data/solar_data.csv")

    features = [
        "temperature",
        "humidity",
        "irradiance",
        "cloud_cover",
        "wind_speed",
        "panel_temperature"
    ]

    actual = data["energy_output"]
    predicted = model.predict(data[features])

    plt.figure(figsize=(10, 5))

    plt.plot(actual.values, label="Actual Energy")
    plt.plot(predicted, label="Predicted Energy")

    plt.xlabel("Sample")
    plt.ylabel("Energy Output (kWh)")
    plt.title("Actual vs Predicted Solar Energy")

    plt.legend()
    plt.tight_layout()

    plt.savefig("static/energy_chart.png")
    plt.close()

    return render_template(
        "chart.html",
        chart_image="energy_chart.png"
    )


if __name__ == "__main__":
    app.run(debug=True)