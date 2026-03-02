# IoT Anomaly Detection

IU Project: From Model to Production (DLBDSMTP01)
Task 1 – IoT anomaly detection using Isolation Forest deployed with FastAPI and tested using a stream simulator.


This project demonstrates how a machine learning model can be trained and deployed as a REST API service.  
An Isolation Forest model is trained on simulated IoT sensor data and deployed using FastAPI.  
A stream simulator continuously sends sensor values to the API and receives anomaly predictions in real time.

------------------------------------------------------------

## Project Structure

project-root/

app/
└── app.py                  # FastAPI prediction service

scripts/
├── train_model.py          # trains Isolation Forest model
└── stream_simulator.py     # generates and sends sensor data

artifacts/
├── model.joblib            # trained model
└── meta.json               # model metadata

requirements.txt              # project dependencies
README.md                     # project documentation

------------------------------------------------------------

## Requirements

- Python 3.9 or higher
- Virtual environment (recommended)

Dependencies are listed in requirements.txt.

------------------------------------------------------------

## Setup

1. Create and activate virtual environment:

python -m venv venv  
source venv/bin/activate      (Mac/Linux)  
venv\Scripts\activate         (Windows)

2. Install dependencies:

pip install -r requirements.txt

------------------------------------------------------------

## Step 1 – Train the Model

If the model artifacts are not already available:

python scripts/train_model.py

This will generate synthetic sensor data, train the Isolation Forest model, and store the model inside the artifacts folder.

------------------------------------------------------------

## Step 2 – Run the API

uvicorn app.app:app --reload

Open in browser:

http://127.0.0.1:8000  
http://127.0.0.1:8000/docs  

The /docs page provides an interactive Swagger interface for testing the API.

------------------------------------------------------------

## Step 3 – Run the Stream Simulator

(Open a new terminal while the API is running)

python scripts/stream_simulator.py

The simulator sends structured JSON sensor data every 2 seconds and prints the anomaly score returned by the API.

------------------------------------------------------------

## Example API Input

{
  "temperature": 70,
  "humidity": 20,
  "sound_volume": 95
}

## Example API Output

{
  "anomaly_score": 0.78,
  "is_anomaly": 1
}

------------------------------------------------------------

## Reproducibility

The repository contains:
- Complete source code
- Model training script
- API deployment code
- Stream simulator
- Model artifacts

By following the steps above, the full system can be reproduced locally from training to real-time anomaly detection.

------------------------------------------------------------

Developed by Siddharthsinh Rathod  
International University of Applied Sciences
