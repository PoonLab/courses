from urllib import request
from bs4 import BeautifulSoup
import re

def soup2table(element):
    """ A simple function for extracting text from an HTML table in BeautifulSoup """
    for row in element.findAll('tr'):
        data = row.findAll('td')
        yield ([datum.text for datum in data])  # use list comprehension
        

# regex to extract content from <td> elements
pat = re.compile("^([A-Za-z,\s.\&]+)([0-9,]+)\s+\(([0-9,]+\.[0-9]+)\)")
pat2 = re.compile("^([A-Za-z,\s.\&]+)Table")

def get_data(txt):
    """ Extract items from the text field of a <td> element """
    # replace non-breaking space with a regular one
    txt = txt.replace(u'\xa0', ' ')
    
    # apply regex
    matches = pat.findall(txt)
    if not matches:
        # some entries contain a footnote instead of count/rate data
        match2 = pat2.findall(txt)
        if not match2:
            return None, None, None
        return match2[0], None, None
        
    cause, count, rate = matches[0]
    
    cause = re.sub("\s+", ' ', cause)  # remove extra whitespace
    count = int(count.replace(',', ''))  # convert 1,000 to 1000
    rate = float(rate.replace(',', ''))
    
    return cause, count, rate


response = request.urlopen('http://www.phac-aspc.gc.ca/publicat/lcd-pcd97/table1-eng.php')
src = response.read()
soup = BeautifulSoup(src, 'html.parser')

tables = soup.findAll('table')

# store the results as a list
results = []

for row in soup2table(tables[0]):
    if len(row) < 13:
        continue  # go to next row
        
    rank = row[0]  # e.g., "1st"
    result = [get_data(txt) for txt in row[1:]]
    results.append(result)

print (results)
