import requests
import urllib3
import re
from bs4 import BeautifulSoup

url = 'https://horriblesubs.info/api.php?method=getshows&type=show&showid=1206'
response = requests.get(url, timeout=5)
link =  []

# scrapes the whole page
content = BeautifulSoup(response.content, "html.parser")

# tries to identify the specific torrent links under the hs-torrent-link class
for torrent in content.find_all(class_="rls-link link-1080p"):
    for link in torrent.find_all('a', attrs={'href': re.compile("^magnet:")}):
        link.append(link.get('href'))
        print (link)




