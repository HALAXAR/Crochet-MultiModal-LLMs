from dotenv import load_dotenv
load_dotenv() 
import os
from PIL import Image
import google.generativeai as genai
local_api_key =  os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=local_api_key)
file_path = "F:\example-bill.jpeg"

#creating a class for Gemini model which encapsulates individual function definitions in the global scope
#here the the term self refers to the object instantiated in the future 

class Gemini_model:
    #when we call the class Gemini_model() we need to give generated_api_key and file_path as arguments
    def __init__(self, generated_api_key, file_path):
        self.apikey = generated_api_key #here we set the new object property apikey from the argument generated_api_key
        self.filepath = file_path #setting new object property filepath from the argument file_path
        #self.genai = genai.configure(api_key=generated_api_key) here setting the genai property after configuring the genai model from the passed api key

    def welcome_statement(self):
        print("-"*10+"GEMINI-VISION-APPLICATION"+"-"*10)        
    def load_image(self):
        img = Image.open(self.filepath)
        self.currentimage = img

    def handle_input_prompt(self):
        prompt = input("Enter your prompt :")
        self.currentprompt = prompt

    def handle_gemini_response(self):
        model = genai.GenerativeModel("gemini-pro-vision")
        response = None
        if self.currentprompt != "":
            response = model.generate_content([self.currentprompt, self.currentimage])
        else:
            response = model.generate_content(self.currentimage)
        self.currentresponse = response.text

    def display_response(self):
        print(self.currentresponse)
    

#now as we instantiate stuff, the gemini_instance become the term "self" we used earlier in the class
gemini_instance = Gemini_model(local_api_key, file_path)
gemini_instance.welcome_statement()
gemini_instance.load_image()
gemini_instance.handle_input_prompt()
gemini_instance.handle_gemini_response()
gemini_instance.display_response()
