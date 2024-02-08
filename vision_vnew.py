## To run the following code you need to create a virtual environment and the defing a ".env" file that would store your API key for safety purposes
## Run the following commands in you Command Prompt for accessing the following Python Script without any problems
## Command for creating a virtual environment: >conda create -p venv python==3.11 -y
## Command for installing required packages
   # >pip install google-generativeai
   # >pip install python-dotenv

## Visit "https://makersuite.google.com/app/apikey" for generating your own api key
   # Copy the API key and create a .env file in the same file directory and write the following in the .env file 
      # GOOGLE_API_KEY="paste_your_api_key_here"

## Accomplishment of the above obejectives are necessary for the using the gemini-pro-vision model

## The main Python Script starts from here...

## Importing required libraries
from dotenv import load_dotenv   # load_dotenv() is used to load all the environment variables
load_dotenv() 
import os
from PIL import Image
import google.generativeai as genai



## Fetching the API key using the os library
local_api_key =  os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=local_api_key)
## Provide with the path of the file in the variable file_path
   # Use the one below as a reference for the format use '//'
file_path = "C:\\Users\\haria\\OneDrive\\Desktop\\Data Science\\images\\images\\ffbf0023_p0.jpg"

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


## the below model opens the image (the term open computationally refers to reading the encoded pixel values of the image from the sources like .jpg, png, , .bmp and others) 
    def load_image(self):
        img = Image.open(self.filepath)
        self.currentimage = img


## This method is used to get questions from the user that would serve as prompt for the generation of an output

    def handle_input_prompt(self):
        prompt = input("Enter your prompt :")
        self.currentprompt = prompt




##This is the method that is being used for the generation of a response from the gemini-pro-vision model
        
    def handle_gemini_response(self):
        model = genai.GenerativeModel("gemini-pro-vision") #Mentioning the Gemini model that is being used
        response = None 
        # There can be two cases
        # 1. A prompt is provided i.e. a question is being asked from the gemini pro vision model, based on which it has to generate and output
        # 2. No prompt provided hence, it the model needs to generate an output based on the understanding of the file provided 
        if self.currentprompt != "": # Checking if the response is empty or not
            response = model.generate_content([self.currentprompt, self.currentimage]) # If not empty then generating output based on the provided prompt and image
        else:
            response = model.generate_content(self.currentimage) # Else just generating the output based on the understanding of the model for the particular file provided
        self.currentresponse = response.text # Storing the text-response generated 

    def display_response(self):
        print(self.currentresponse) # Displaying the generated response

    

#now as we instantiate stuff, the gemini_instance become the term "self" we used earlier in the class
gemini_instance = Gemini_model(local_api_key, file_path)
gemini_instance.welcome_statement()
gemini_instance.load_image()
gemini_instance.handle_input_prompt()
gemini_instance.handle_gemini_response()


gemini_instance.display_response()

