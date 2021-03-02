import requests
from lxml import etree

class FryingPan(object):

    def __init__(self, url, find_string):
        self.url = url
        self.find_string = find_string

    def get_french_toast(self):
        content = requests.get(self.url).content.decode('utf-8')
        tree = etree.fromstring(content)
        status = tree.find(self.find_string)
        return status.text

