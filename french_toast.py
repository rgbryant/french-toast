from __future__ import print_function
from lxml import etree
import requests

def get_french_toast():

    page = requests.get('http://www.universalhub.com/toast.xml')
    tree = etree.fromstring(page.content)

    status = tree.find('status')

    return status.text

if __name__ == "__main__":
    print(get_french_toast())
