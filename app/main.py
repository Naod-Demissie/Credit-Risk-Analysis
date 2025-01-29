from fastapi import FastAPI, HTTPException
import pickle
import pandas as pd
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Load the trained model
MODEL_PATH = "../checkpoint/best_model.pkl"
try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")


# Define API endpoints
@app.post("/predict")
def predict(input_data):
    try:
        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data.dict()])

        # Make prediction
        prediction = model.predict(input_df)

        # Return response
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")


# Root endpoint
@app.get("/")
def home():
    return {"message": "Model Serving API is running"}
