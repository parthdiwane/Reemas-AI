import os 
import shutil

images = [f for f in os.listdir() if '.png' in f.lower()]


for images in images:
    new_path = 'src/assets/storedImgs'
    shutil.move(images, new_path)
    