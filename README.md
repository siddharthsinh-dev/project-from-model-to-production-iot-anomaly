# IoT Anomaly Detection – Isolation Forest

IU Project: From Model to Production (DLBDSMTP01)  
Task 1 – IoT anomaly detection using Isolation Forest deployed with FastAPI and tested using a stream simulator.

## Project Structure

app/ → FastAPI application (prediction API)  
scripts/train_model.py → trains Isolation Forest model  
scripts/stream_simulator.py → generates sample sensor data  
artifacts/ → trained model and metadata  
requirements.txt → project dependencies  

## Setup Instructions

1. Create virtual environment:

python -m venv venv  
source venv/bin/activate  

2. Install dependencies:

pip install -r requirements.txt  

## Train Model (if needed)

python scripts/train_model.py  

## Run API

uvicorn app.app:app --reload  

Open in browser:
http://127.0.0.1:8000  
http://127.0.0.1:8000/docs  

## Run Stream Simulator (inside new terminal)

python scripts/stream_simulator.py  

The simulator sends simulated IoT sensor data and receives anomaly predictions.