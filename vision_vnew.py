from dotenv import load_dotenv
load_dotenv() 
import os
from PIL import Image
import google.generativeai as genai
local_api_key =  os.getenv("GOOGLE_API_KEY")

file_path = "F:\example-bill.jpeg"



class Gemini_model:
    def __ini__(self, generated_api_key, file_path):
        self.apikey = generated_api_key
        self.filepath = file_path
        self.genai = genai.configure(api_key=generated_api_key)

    def welcome_statement(self):
        print("-"*10+"GEMINI-VISION-APPLICATION"+"-"*10)        
    def load_image(self):
        img = Image.open(self.filepath)
        self.currentimage = img

    def handle_input_prompt(self):
        prompt = input("Enter your prompt :")
        self.currentprompt = prompt

    def handle_gemini_response(self):
        model = self.genai.GenerativeModel("geminipro-vision")
        response = None
        if self.currentprompt != "":
            response = model.generate_content([self.currentprompt, self.currentimage])
        else:
            response = model.generate_content(self.currentimage)
        self.currentresponse = response.text

    def display_response(self):
        print(self.currentresponse)
    

gemini_instance = Gemini_model(local_api_key, file_path)
gemini_instance.welcome_statement()
gemini_instance.load_image()
gemini_instance.handle_input_prompt()
gemini_instance.handle_gemini_response()
gemini_instance.display_response()
