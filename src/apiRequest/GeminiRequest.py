import os
from dotenv import load_dotenv, dotenv_values  
import google.generativeai as genai
from GoogleVision import detect_text

load_dotenv() 

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        {"role": "user", "parts": "A client that is asking a question about whether or not something a certain political figure is saying is true or not"},
        {"role": "model", "parts": "You are a system that is tasked to verify if what the political figure is saying is true or false."},
        {"role": "model", "parts": "The current major information available is that Joe Biden has dropped out of the election and has been replaced by Kamala Harris. Donald Trump is still representing the Republicans. The VP for the Democrats is Tim Walz and the VP for the Republicans is JD Vance."},
    ]
)

img_path = 'src/assets/imgs/v1.png'

print('Hello, please state the name of the person talking and any other necessary context: ')
context = input()

txt_from_img = detect_text(img_path)
print('Extracted text from image: ' + txt_from_img)
print('\n')

response = chat.send_message(f"Context: {context}. Verify the following fact: {txt_from_img}. State only whether the fact is true, false, unsure, or not enough information provided. Do not explain why the fact is true or false. Please keep your responses limited to the four options given.")

print("Output: " + response.text)
print("Please note that this AI's information on CURRENT events is limited.")

