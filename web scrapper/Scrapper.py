from bs4 import BeautifulSoup
import requests

url = 'https://horriblesubs.info/shows/mob-psycho-100-s2/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

print (content)