from dotenv import load_dotenv  
load_dotenv() 
import os
from PIL import Image
import google.generativeai as genai
import json
local_api_key =  os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=local_api_key)
file_path = "C:\\Users\\haria\\OneDrive\\Desktop\\Crochet-Multimodal-LLMs\\images\\images"


class Gemini_model:

  def __init__(self, generated_api_key, file_path):
    self.apikey = generated_api_key 
    self.filepath = file_path 
        

  def welcome_statement(self):
    print("-"*20+"GEMINI-VISION-APPLICATION"+"-"*20)        
    print("\n")


  def load_data(self):
    with open('train_v1.json') as f:
      self.dataset = json.load(f)


  def handle_gemini_response(self):
    model = genai.GenerativeModel("gemini-pro-vision") 
    response = None 
    if self.currentprompt != "":
      response = model.generate_content([self.currentprompt, self.currentimage]) 
    else:
      response = model.generate_content(self.currentimage) 
    self.currentresponse = response.text


  def submission_format(self):
    self.submit_data={"questionId":self.questionID,"answer":self.currentresponse,"answer_page":self.pageId}
    self.new_data.append(self.submit_data)


  def get_image_dir(self):
    self.image_dir=self.filepath+"\\"+self.pageId+".jpg"
    self.currentimage = Image.open(self.image_dir)


  def main_process(self):
    self.new_data=[]
    for self.sample in self.dataset['data']:
      self.pageId=self.sample['page_ids'][0]
      self.currentprompt = self.sample["question"]
      self.questionID=self.sample["questionId"]
      self.get_image_dir()
      print("Given prompt: ",self.currentprompt)
      self.handle_gemini_response()
      print("Response Generated: ",self.currentresponse)
      self.submission_format()
      print("\n")


  def dumping_data(self):
    with open('submission.json','w') as f:
     json.dump(self.new_data,f)



gemini_instance = Gemini_model(local_api_key, file_path)
gemini_instance.welcome_statement()
gemini_instance.load_data()
gemini_instance.main_process()
gemini_instance.dumping_data()
