import time
import random
import requests

API_URL = "http://127.0.0.1:8000/predict"

def generate_sensor_data():
    """
    Generate simulated IoT sensor data.
    Most of the time values are normal.
    Sometimes we inject anomalies.
    """

    # 80% normal data
    if random.random() < 0.8:
        return {
            "temperature": random.randint(35, 50),
            "humidity": random.randint(40, 70),
            "sound_volume": random.randint(50, 75)
        }
    # 20% anomaly data
    else:
        return {
            "temperature": random.randint(65, 85),
            "humidity": random.randint(10, 30),
            "sound_volume": random.randint(85, 100)
        }

def main():
    print("Starting IoT Stream Simulator...\n")

    while True:
        data = generate_sensor_data()

        try:
            response = requests.post(API_URL, json=data)
            result = response.json()

            print("Sent:", data)
            print("Received:", {
                "anomaly_score": round(result["anomaly_score"], 4),
                "is_anomaly": result["is_anomaly"]
            })
            print("-" * 50)

        except Exception as e:
            print("Error communicating with API:", e)

        time.sleep(2)  # wait 2 seconds before next data point


if __name__ == "__main__":
    main()