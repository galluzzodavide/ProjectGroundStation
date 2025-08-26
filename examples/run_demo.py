from epd import run_pipeline

if __name__ == "__main__":
    obs = {
        "temperature": [292.5],
        "wind_u": [3.2],
        "wind_v": [-1.4],
        "pressure": [1010.0],
    }
    preds = run_pipeline(obs, steps=5)
    print("Predictions after 5 steps:")
    for k, v in preds.items():
        print(f"  {k}: {v:.3f}")

#prova prova prova