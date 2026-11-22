
from pathlib import Path
from transformers import pipeline

# Model is initially not loaded
classifier = None


def load_disease_model():
    global classifier

    if classifier is None:
        print("Loading plant disease detection model...")

        classifier = pipeline(
            "image-classification",
            model="neghani/plantvillage-mobilenetv2",
            device=-1
        )

    return classifier


def detect_disease(image_path):

    image_path = Path(image_path).resolve()

    if not image_path.exists():
        raise FileNotFoundError(
            f"Image not found: {image_path}"
        )

    model = load_disease_model()

    predictions = model(str(image_path), top_k=None)

    best_prediction = predictions[0]

    return {
        "disease": best_prediction["label"],
        "confidence": round(best_prediction["score"], 4),
        "predictions": predictions,
        "note": (
            "This is an AI-based preliminary screening result. "
            "Confirm with an agricultural expert before treatment."
        )
    }
