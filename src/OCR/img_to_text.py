import pytesseract
import cv2
from serpapi import GoogleSearch
import json



params = {
    'api_key': '',
    'engine': 'google_lens',
    'url': 'https://user-images.githubusercontent.com/81998012/210290011-c175603d-f319-4620-b886-1eaad5c94d84.jpg',
    'hl': 'en',
}

search = GoogleSearch(params)                   # data extraction on the SerpApi backend
google_lens_results = search.get_dict()         # JSON -> Python dict

del google_lens_results['search_metadata']
del google_lens_results['search_parameters']

print(json.dumps(google_lens_results, indent=2, ensure_ascii=False))