from Flask import Flask
import random

app = Flask(__name__)

# Simulate environmental parameters
def get_temperature():
    return round(random.uniform(18, 35), 2)

def get_humidity():
    return round(random.uniform(40, 90), 2)

def get_soil_moisture():
    return round(random.uniform(20, 80), 2)

@app.route("/")
def get_environmental_data():
    data = {
        "temperature (°C)": get_temperature(),
        "humidity (%)": get_humidity(),
        "soil_moisture (%)": get_soil_moisture()
    }
    
    alert = []
    if data["soil_moisture (%)"] < 30:
        alert.append("⚠️ Soil is too dry. Irrigation recommended.")
    if data["temperature (°C)"] > 32:
        alert.append("⚠️ High temperature. Consider shading.")
    
    result = f"Smart Agriculture Readings:<br><br>"
    for key, value in data.items():
        result += f"{key}: {value}<br>"
    
    if alert:
        result += "<br><strong>Alerts:</strong><br>"
        for message in alert:
            result += f"{message}<br>"

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
