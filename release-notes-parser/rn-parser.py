from bs4 import BeautifulSoup
import urllib3
import re
import requests

url = 'http://chpsp/IST/Lists/Release%20Notes/AllItems.aspx'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')

reportLinks = soup.find_all('a', attrs={'href': re.compile("^/listform")})
linksList = []
titlesList = []

for link in reportLinks:
	linksList.append(link.get('href'))

for title in reportLinks:
	titlesList.append(title.get('title'))
