import feedparser
import urllib3, shutil

url = 'http://chpsp/IST/_layouts/listfeed.aspx?List=%7B6FBBF0B5%2D75BF%2D49B1%2DB0F6%2DA7B3C7801857%7D&Source=http%3A%2F%2Fchpsp%2FIST%2FLists%2FRelease%2520Notes%2FAllItems%2Easpx'

c = urllib3.PoolManager()

filename = "release-notes-feed.xml"

with c.request('GET', url, preload_content=False) as res, open(filename, 'wb') as out_file:
	shutil.copyfileobj(res, out_file)
