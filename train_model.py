import os
import sys
from pymongo import MongoClient
from datetime import datetime, timezone
from noshow_iq.preprocess import load_and_clean, get_features
from noshow_iq.model import train

if __name__ == "__main__":
    # Find dataset
    paths = [
        "data/KaggleV2-May-2016.csv",
        "noshow_iq/data/KaggleV2-May-2016.csv",
    ]
    dataset_path = None
    for p in paths:
        if os.path.exists(p):
            dataset_path = p
            break

    if not dataset_path:
        print("Dataset not found!")
        sys.exit(1)

    print("Loading dataset...")
    df = load_and_clean(dataset_path)
    X, y = get_features(df)

    print("Training model...")
    model, metrics = train(X, y)

    try:
        MONGO_URI = os.getenv("MONGO_URI")
        if not MONGO_URI:
            raise ValueError("MONGO_URI not set")
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        client.server_info()
        db = client["noshow_iq"]
        db["training_runs"].insert_one({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "training_size": len(X),
            "imbalance_technique": "SMOTE + class_weight=balanced",
            "metrics": metrics,
        })
        print("Training run saved to MongoDB!")
    except Exception as e:
        print(f"MongoDB skipping: {e}")

    print("Training complete!")
    print(metrics)