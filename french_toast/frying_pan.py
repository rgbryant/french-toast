import requests
from lxml import etree

class FryingPan(object):

    def __init__(self, url, find_string):
        self.url = url
        self.find_string = find_string

    def get_french_toast():
        page = requests.get(self.url)
        tree = etree.fromstring(page.content)
        return status.text

