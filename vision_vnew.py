from dotenv import load_dotenv
load_dotenv() 
import os
from PIL import Image
import google.generativeai as genai
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

print("-"*10+"GEMINI-VISION-APPLICATION"+"-"*10)
file_path="F:\example-bill.jpeg"
img =Image.open(file_path)
Input=input("Input Prompt: ")
response=get_gemini_response(Input,img)
print(response)