import requests
import urllib3
import torrentool
import re

from bs4 import BeautifulSoup

url = 'https://horriblesubs.info/api.php?method=getshows&type=show&showid=1206'
response = requests.get(url, timeout=5)

# scrapes the whole page
content = BeautifulSoup(response.content, "html.parser")

# tries to identify the specific links under the rls--link class
for torrent in content.find_all(class_="rls-link link-1080p"):
    for link in torrent.find_all('a', attrs={'href':re.compile("^https")}, title="Torrent Link"):
        print (link.get('href'))



# transform magnet links into torrent files
