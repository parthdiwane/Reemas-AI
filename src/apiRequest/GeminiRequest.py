import os
import google.generativeai as genai
from GoogleVision import *
import colorama
from colorama import Fore, Style

colorama.init()

genai.configure(api_key=os.environ['API_KEY_GEMINI'])

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        {"role": "user", "parts": "A client that is asking a question about whether or not something a certain politcal figure is saying is true or not"},
        {"role":"model", "parts": "You are a system that is tasked to verfiy if what the poltical figure is saying is true or false."},
        {"role":"model", "parts":"The current major information aviable is that Joe Biden has dropped out of the election and has been replaced by kamal harris. Donald trump is still representing the republicans. The VP for the democrats is Tim Walz and the VP for the republicans is JD Vance"},
    ]
)

img_path = 'src/assets/imgs/false.png'

print(Fore.BLUE + 'hello, please state the name of the person talking and any other nessassry context: ')
context = input()

txt_from_img = detect_text(img_path)
print("\n")
print(Fore.GREEN + 'verifying: ' + detect_text(img_path))

print('\n')
responce = chat.send_message("context: " + context + " verify the following fact: " + txt_from_img + " . State only whether if the fact is true, false, unsure, or not enough information provided. Do not explain why the fact is true or false. Please keep you responces limited to the four options given")
print(Fore.RED + "Output: " +responce.text)
print(Fore.MAGENTA + "Please note that this AI information on CURRENT information is limited.")
print(Fore.RESET)



