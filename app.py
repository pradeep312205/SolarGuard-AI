from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import json

app = Flask(__name__)

# Load trained ML model
model = joblib.load("model/solar_model.pkl")

# Load maintenance knowledge
with open("knowledge/maintenance.json", "r") as file:
    maintenance_data = json.load(file)


@app.route("/")
def home():
    return render_template("index.html")


# Solar energy prediction + maintenance connection
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

    # Predict solar energy output
    prediction = float(model.predict(input_data)[0])
    prediction = round(prediction, 2)

    # Determine maintenance requirement
    # This threshold is used for the project prototype.
    LOW_OUTPUT_THRESHOLD = 10.0

    if prediction < LOW_OUTPUT_THRESHOLD:

        maintenance_status = "Maintenance Attention Recommended"

        maintenance_item = maintenance_data.get(
            "low_output",
            maintenance_data["general"]
        )

        maintenance_title = maintenance_item["title"]

        maintenance_steps = maintenance_item["steps"]

    else:

        maintenance_status = "Normal Output"

        maintenance_item = maintenance_data.get(
            "general",
            {}
        )

        maintenance_title = "Routine Maintenance"

        maintenance_steps = maintenance_item.get(
            "steps",
            []
        )

    return jsonify({
        "predicted_energy": prediction,
        "maintenance_status": maintenance_status,
        "maintenance_title": maintenance_title,
        "maintenance_steps": maintenance_steps
    })


# Maintenance chatbot
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


# Solar analytics page
@app.route("/analytics")
def analytics():
    return render_template(
        "chart.html",
        chart_image="energy_chart.png"
    )


if __name__ == "__main__":
    app.run(debug=True)