import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("Write a poem on love in the style of the author Fyodor Dostoevsky")

print(response.text)