from google.cloud import vision
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '814c4dbd41c403783ba8f7e8c0b221d3b785db24.json'

def detect_text(path):
    """Detects text in the given image."""
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    if len(texts) > 0:
        print(texts[0].description)
    else:
        print('No text detected.')

image_path = 'image.png'
detect_text(image_path)
