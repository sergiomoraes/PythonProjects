from bs4 import BeautifulSoup
import requests
import urllib3

url = 'https://horriblesubs.info/shows/mob-psycho-100-s2/'
response = requests.get(url, timeout=5)
# scrapes the whole page
content = BeautifulSoup(response.content, "html.parser")
# tries to identify the specific torrent links under the hs-torrent-link class
torrent = content.find(class_="dl-type hs-torrent-link")
for links in torrent.next_element():
    print(links['href'])
