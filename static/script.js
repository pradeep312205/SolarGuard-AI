async function predictEnergy() {

    const temperature = document.getElementById("temperature").value;
    const humidity = document.getElementById("humidity").value;
    const irradiance = document.getElementById("irradiance").value;
    const cloudCover = document.getElementById("cloud_cover").value;
    const windSpeed = document.getElementById("wind_speed").value;
    const panelTemperature = document.getElementById("panel_temperature").value;

    const result = document.getElementById("result");

    result.innerHTML = "Predicting...";

    try {

        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                temperature: temperature,
                humidity: humidity,
                irradiance: irradiance,
                cloud_cover: cloudCover,
                wind_speed: windSpeed,
                panel_temperature: panelTemperature
            })
        });

        const data = await response.json();

        let maintenanceHTML = "";

        if (data.maintenance_steps && data.maintenance_steps.length > 0) {

            maintenanceHTML = `
                <h3>${data.maintenance_title}</h3>
                <ol>
                    ${data.maintenance_steps.map(step => `<li>${step}</li>`).join("")}
                </ol>
            `;
        }

        result.innerHTML = `
            <h2>Prediction Result</h2>

            <p>
                <strong>Predicted Energy Output:</strong>
                ${data.predicted_energy} kWh
            </p>

            <p>
                <strong>Maintenance Status:</strong>
                ${data.maintenance_status}
            </p>

            <div class="maintenance-result">
                ${maintenanceHTML}
            </div>
        `;

    } catch (error) {

        console.error(error);

        result.innerHTML = `
            <p>
                Unable to get prediction. Please try again.
            </p>
        `;
    }
}


async function askAssistant() {

    const question = document.getElementById("question").value;

    const chatResult = document.getElementById("chatResult");

    if (!question.trim()) {

        chatResult.innerHTML =
            "Please enter a maintenance question.";

        return;
    }

    chatResult.innerHTML = "Assistant is processing...";

    try {

        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        });

        const data = await response.json();

        chatResult.innerHTML =
            `<pre>${data.answer}</pre>`;

    } catch (error) {

        console.error(error);

        chatResult.innerHTML =
            "Unable to connect to the maintenance assistant.";
    }
}