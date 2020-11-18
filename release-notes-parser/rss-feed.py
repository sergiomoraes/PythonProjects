from bs4 import BeautifulSoup
import requests
from getpass import getpass
from requests_ntlm import HttpNtlmAuth
import re

# Authentication
url = 'http://chpsp/IST/_layouts/listfeed.aspx?List=%7B6FBBF0B5%2D75BF%2D49B1%2DB0F6%2DA7B3C7801857%7D&Source=http%3A%2F%2Fchpsp%2FIST%2FLists%2FRelease%2520Notes%2FAllItems%2Easpx'
url_get = requests.get(
   url, 
   auth=HttpNtlmAuth('sergio.moraes@chpw.org', getpass())
)

# Prints the the response message. Hopefully 200.
print(url_get)

# Creates the soup
soup = BeautifulSoup(url_get.content, 'lxml')

# Searching an parsing
#col_all = soup.item.get_text()
#print(col_all)


#for link in col_all:
#   print(link.get('b'))

this_week = soup.find_all('pubDate', sring=re.compile('Nov 03',recursive=True))

for pubDate in BeautifulSoup:
   print(soup.item.get_text())