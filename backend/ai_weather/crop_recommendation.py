
import pandas as pd
import joblib
from huggingface_hub import hf_hub_download

model = None
label_encoder = None


def load_crop_model():
    global model, label_encoder

    if model is None:
        print("Loading crop recommendation model...")

        model_path = hf_hub_download(
            repo_id="coderprem/crop-recommendation",
            filename="soil.pkl"
        )

        encoder_path = hf_hub_download(
            repo_id="coderprem/crop-recommendation",
            filename="label_encoder.pkl"
        )

        model = joblib.load(model_path)
        label_encoder = joblib.load(encoder_path)

    return model, label_encoder


def recommend_crop(n, p, k, temperature, humidity, ph, rainfall):

    crop_model, encoder = load_crop_model()

    inputs = pd.DataFrame(
        [[n, p, k, temperature, humidity, ph, rainfall]],
        columns=[
            "N", "P", "K", "temperature",
            "humidity", "ph", "rainfall"
        ]
    )

    prediction = crop_model.predict(inputs)
    crop = encoder.inverse_transform(prediction)

    return {
        "recommended_crop": str(crop[0])
    }
