import sharepy

s = sharepy.connect("chpwa.sharepoint.com", username="sergio.moraes@chpw.org", password="s1bm2nd3P0eGr33n", auth_tld="login.microsoftonline.com")

open('c:\\Users\\Sergio.Moraes\\Documents\\Github\\PythonProjects\\release-notes-parser\\feed.txt', 'wb').write(myfile)
