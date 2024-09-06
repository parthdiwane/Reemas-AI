from google.cloud import vision

def detect_text(path):
    """Detects text in the given image.

    Args:
      path: The path to the image file.

    Returns:
      A list of detected text annotations.
    """

    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations


    return texts

# Replace 'path/to/your/image.jpg' with the actual path to your image
path = 'image.png'
texts = detect_text(path)

for text in texts:
    print(text.description)
