from google.cloud import vision
import os 

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "src/apiRequest/creds.json"
def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()
    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    full_text = "" #starts as empty string to store all text
    
    if texts:
        for text in texts:
            full_text += text.description + " " #put space between each word
            full_text.strip() #print full text, while removing any trailing space
            
    else:
        full_text= "No text found in the image."
        return full_text
    return full_text