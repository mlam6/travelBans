from urllib.request import urlopen
from bs4 import BeautifulSoup

html = 'https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html/'

page = urlopen(html)

data = BeautifulSoup(page, 'html.parser')

travelBans = []
table = data.find('table')
table_body = table.find('tbody')
rows = table_body.findAll('tr') 

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data2.append([ele for ele in cols if ele])
    
for travelBan in travelBans:
    print(travelBan)
