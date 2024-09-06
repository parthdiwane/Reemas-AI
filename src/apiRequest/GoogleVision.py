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
    print('Texts:')
    for text in texts:
        print('\n"{}"'.format(text.description))
        vertices = [f'({vertex.x},{vertex.y})' for vertex in text.bounding_poly.vertices]
        print('bounds: {}'.format(','.join(vertices)))
    if response.error.message:
        raise Exception(f'{response.error.message}\nFor more info on error messages, check: https://cloud.google.com/apis/design/errors')

# Replace 'PATH_TO_YOUR_IMAGE' with the path to the image file you want to analyze.
detect_text('src/assets/imgs/test.png')