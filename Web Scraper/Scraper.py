__author__ = 'Chandler'

import requests
import BeautifulSoup

url= 'http://www.pcmag.com/article2/0,2817,2369981,00.asp'
response = requests.get(url)
html = response.content
print html
