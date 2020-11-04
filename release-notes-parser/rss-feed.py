from bs4 import BeautifulSoup
import requests
from getpass import getpass
from requests_ntlm import HttpNtlmAuth
 
url = 'http://chpsp/IST/Lists/Release%20Notes/AllItems.aspx'
url_get = requests.get(
   url, 
   auth=HttpNtlmAuth('sergio.moraes@chpw.org', getpass())
)
print(url_get)
soup = BeautifulSoup(url_get.content, 'lxml')
col = soup.find('div', class_="column_main")
col_all = soup.find_all('a')
for link in col_all:
   print(link.get('href'))