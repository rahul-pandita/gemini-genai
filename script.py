import google.generativeai as genai
import os
import PIL.Image

img = PIL.Image.open("calc.jpg")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")

response = model.generate_content(["The following image contains an image of a mathematics problem written in human handwriting. Give a detailed step by step solution to the problem. Also identify the branch of mathematics to which this problem belongs", img])

print(response.text)
