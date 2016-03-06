__author__ = 'Chandler'

import requests
from BeautifulSoup import BeautifulSoup

url= 'http://www.pcmag.com/article2/0,2817,2369981,00.asp'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class': 'stripe'})
print table.prettify()
#print soup.prettify()