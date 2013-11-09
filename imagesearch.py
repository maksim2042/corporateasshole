import json
import os
import time
import requests
from requests.exceptions import ConnectionError

import pudb
 
def get_image(query):
    """Download full size images from Google image search.

    Don't print or republish images without permission.
    I used this to train a learning algorithm.
    """
    BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?'\
             'v=1.0&q=' + query + '&start=0'

 
    r = requests.get(BASE_URL)
    image_info = json.loads(r.text)['responseData']['results'][0]
    url = image_info['unescapedUrl']
    return url