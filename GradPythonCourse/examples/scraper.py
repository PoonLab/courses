from urllib import request
from bs4 import BeautifulSoup
import re

def soup2table(element):
    """ A simple function for extracting text from an HTML table in BeautifulSoup """
    for row in element.findAll('tr'):
        data = row.findAll('td')
        yield ([datum.text for datum in data])  # use list comprehension
        

# regex to extract content from <td> elements
pat = re.compile("^([A-Za-z,\s.]+)([0-9]+)\s+\(([0-9]+\.[0-9]+)\)$")
        
response = request.urlopen('http://www.phac-aspc.gc.ca/publicat/lcd-pcd97/table1-eng.php')
src = response.read()
soup = BeautifulSoup(src)

tables = soup.findAll('table')

for result in soup2table(tables[0]):
    if len(result) < 13:
        continue  # go to next row
        
