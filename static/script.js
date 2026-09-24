async function predictEnergy() {

    const data = {
        temperature: document.getElementById("temperature").value,
        humidity: document.getElementById("humidity").value,
        irradiance: document.getElementById("irradiance").value,
        cloud_cover: document.getElementById("cloud_cover").value,
        wind_speed: document.getElementById("wind_speed").value,
        panel_temperature: document.getElementById("panel_temperature").value
    };

    try {

        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        document.getElementById("result").innerHTML =
            "Predicted Energy Output: " +
            result.predicted_energy +
            " kWh";

    } catch (error) {

        document.getElementById("result").innerHTML =
            "Error making prediction.";

        console.error(error);
    }
}
async function askAssistant() {

    const question = document.getElementById("chatQuestion").value;

    if (!question.trim()) {

        document.getElementById("chatResponse").innerText =
            "Please enter a question.";

        return;
    }

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

        const result = await response.json();

        document.getElementById("chatResponse").innerText =
            result.answer;

    } catch (error) {

        document.getElementById("chatResponse").innerText =
            "Unable to connect to the maintenance assistant.";

        console.error(error);
    }
}