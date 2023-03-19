import base64
import requests


def get_as_base64(url):

    img = base64.b64encode(requests.get(url).content)
   # base64.b64encode(requests.get(url).content).decode('utf-8')

    return img.decode('utf-8')