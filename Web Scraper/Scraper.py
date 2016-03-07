__author__ = 'Chandler'

import requests
from BeautifulSoup import BeautifulSoup

url= 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
#print soup.prettify()
table = soup.find('tbody', attrs={'class': 'stripe'})
print table.prettify()