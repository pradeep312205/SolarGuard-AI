from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import json
import os

app = Flask(__name__)

# Load trained ML model
model = joblib.load("model/solar_model.pkl")

# Load maintenance knowledge
with open("knowledge/maintenance.json", "r") as file:
    maintenance_data = json.load(file)


# Load maintenance schedules
SCHEDULE_FILE = "maintenance_schedule.json"

if os.path.exists(SCHEDULE_FILE):
    with open(SCHEDULE_FILE, "r") as file:
        schedules = json.load(file)
else:
    schedules = []


@app.route("/")
def home():
    return render_template("index.html")


# ---------------------------------------------------------
# Solar energy prediction + maintenance connection
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# Fault Diagnosis + Maintenance Assistant
# ---------------------------------------------------------

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json(silent=True) or {}
    question = data.get("question", "").lower().strip()

    if not question:
        return jsonify({
            "answer": "Please enter a maintenance question."
        })

    # Keep the assistant focused on solar-system diagnosis and maintenance.
    solar_scope_terms = (
        "solar", "panel", "photovoltaic", "pv array", "solar array",
        "inverter", "energy output", "power output", "generation",
        "irradiance", "maintenance", "fault", "troubleshoot",
        "troubleshooting", "error code", "warning", "cleaning",
        "dust", "shading", "crack", "damaged panel", "electrical",
        "electric shock", "wiring", "cable", "safety", "safe",
    )

    if not any(term in question for term in solar_scope_terms):
        return jsonify({
            "answer": (
                "I can help with solar system fault diagnosis, maintenance "
                "guidance, troubleshooting steps, and safety recommendations. "
                "Please ask a question about your solar panels or related equipment."
            )
        })

    best_match = None

    # Search maintenance knowledge
    for item in maintenance_data.values():

        for keyword in item["keywords"]:

            if keyword.lower() in question:
                best_match = item
                break

        if best_match:
            break

    # Use general maintenance guidance if no specific match
    if best_match is None:
        best_match = maintenance_data["general"]

    # Fault diagnosis information
    fault_title = best_match["title"]

    if any(term in question for term in ("safety", "safe", "shock", "hazard", "electrical")):
        assistance_area = "Safety Recommendations"
    elif any(term in question for term in ("troubleshoot", "troubleshooting", "not working", "error", "warning")):
        assistance_area = "Troubleshooting Steps"
    elif any(term in question for term in ("maintenance", "clean", "dust", "inspect", "inspection", "shading")):
        assistance_area = "Maintenance Guidance"
    else:
        assistance_area = "Fault Diagnosis"

    response = f"{assistance_area}\n\n"
    response += f"Identified Issue: {fault_title}\n\n"

    response += "Recommended Maintenance Steps:\n"

    for number, step in enumerate(best_match["steps"], start=1):
        response += f"{number}. {step}\n"

    response += "\nSafety Guidance:\n"
    response += "Follow the site's safety and isolation procedures before performing maintenance."

    return jsonify({
        "answer": response,
        "fault": fault_title,
        "steps": best_match["steps"]
    })


# ---------------------------------------------------------
# Maintenance Scheduling
# ---------------------------------------------------------

@app.route("/schedule", methods=["POST"])
def schedule():

    data = request.get_json()

    activity = data.get("activity", "").strip()
    date = data.get("date", "").strip()

    if not activity or not date:
        return jsonify({
            "success": False,
            "message": "Please provide both maintenance activity and date."
        })

    schedule_item = {
        "activity": activity,
        "date": date
    }

    schedules.append(schedule_item)

    # Save schedule permanently
    with open(SCHEDULE_FILE, "w") as file:
        json.dump(schedules, file, indent=4)

    return jsonify({
        "success": True,
        "message": "Maintenance scheduled successfully.",
        "activity": activity,
        "date": date
    })


# ---------------------------------------------------------
# View Maintenance Schedules
# ---------------------------------------------------------

@app.route("/schedules", methods=["GET"])
def get_schedules():

    return jsonify({
        "schedules": schedules
    })


# ---------------------------------------------------------
# Solar analytics page
# ---------------------------------------------------------

@app.route("/analytics")
def analytics():

    return render_template(
        "chart.html",
        chart_image="energy_chart.png"
    )


# ---------------------------------------------------------
# Run application
# ---------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
