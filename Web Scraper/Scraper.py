__author__ = 'Chandler'

import csv
import requests
from BeautifulSoup import BeautifulSoup

url= 'http://www.pcmag.com/article2/0,2817,2369981,00.asp'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class': 'roundup-chart'})

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)
print list_of_rows

#Output info to .csv file
outfile = open("./laptopcompare.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
