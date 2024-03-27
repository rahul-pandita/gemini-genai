import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

with open("models.txt", "w") as f:
    for model in genai.list_models():
        if "generateContent" in model.supported_generation_methods:
            f.write(model.name)

