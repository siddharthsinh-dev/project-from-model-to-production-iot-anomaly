import os
import json
from datetime import datetime

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib


def make_fake_sensor_data(n=3000, anomaly_rate=0.05, seed=7):
    rng = np.random.default_rng(seed)

    # normal sensor values (example ranges)
    temp = rng.normal(42, 2, n)          # °C
    hum = rng.normal(55, 5, n)           # %
    sound = rng.normal(65, 3, n)         # dB

    df = pd.DataFrame({
        "temperature": temp,
        "humidity": hum,
        "sound_volume": sound
    })

    # add some anomalies
    k = int(n * anomaly_rate)
    idx = rng.choice(n, k, replace=False)

    df.loc[idx, "temperature"] += rng.normal(12, 3, k)
    df.loc[idx, "humidity"] -= rng.normal(18, 5, k)
    df.loc[idx, "sound_volume"] += rng.normal(15, 4, k)

    return df


def main():
    df = make_fake_sensor_data()

    X = df[["temperature", "humidity", "sound_volume"]].values

    model = IsolationForest(
        n_estimators=200,
        contamination=0.05,
        random_state=7
    )
    model.fit(X)

    # save model
    os.makedirs("artifacts", exist_ok=True)
    joblib.dump(model, "artifacts/model.joblib")

    meta = {
        "model": "IsolationForest",
        "features": ["temperature", "humidity", "sound_volume"],
        "trained_at": datetime.now().isoformat()
    }
    with open("artifacts/meta.json", "w") as f:
        json.dump(meta, f, indent=2)

    scores = -model.score_samples(X)
    print("model saved to artifacts/model.joblib")
    print("score example:", round(float(scores[0]), 4))


if __name__ == "__main__":
    main()