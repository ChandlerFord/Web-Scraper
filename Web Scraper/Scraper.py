__author__ = 'Chandler'

import csv
import requests
from BeautifulSoup import BeautifulSoup

url= 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class': 'stripe'})

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text
        list_of_cells.append(text)
    #print list_of_cells (each persons info printed on new line)
    #Adds the cells to 1 row
    list_of_rows.append(list_of_cells)
#print list_of_rows (Prints out all info on one line)

#Output info to .csv file
outfile = open("./inmates.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)