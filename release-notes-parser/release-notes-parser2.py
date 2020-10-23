# Mechanize
import mechanize
import codecs
import re
import os
from ntlm import HTTPNtlmAuthHandler
from bs4 import BeautifulSoup

def parse_page(url, output):
    global handled, user, password, scrape_recursively, content_div_id, \
           sharepoint_url, wiki_base_url, wiki_index, confluence_space_key, \
           empties, has_images, direct_confluence_entry, add_legacy_link


    passman = mechanize.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, url, user, password)
# create the NTLM authentication handler
    auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)

# create and install the opener
    browser = mechanize.Browser()
    browser.add_handler(auth_NTLM)

# Ignore robots.txt
    browser.set_handle_robots(False)
# retrieve the result
    response = browser.open(url)
    handled.append(url)

    soup = BeautifulSoup(response.read(), "html5lib")
    innerDiv = soup.find("div", id=content_div_id)

    if innerDiv != None:
# iterate over all relative links and update links
        links = innerDiv.find_all("a", href=re.compile("^\/"))
        for link in links:
# scrape link
            if wiki_base_url in link['href']:
                newoutput = link['href'].replace(wiki_base_url, "").replace("%20", "+").replace(".aspx", "")
                fullLink = sharepoint_url + link['href']
                if scrape_recursively and fullLink not in handled:
                    print fullLink
                    parse_page(fullLink, newoutput + ".md")

# fix links to point to Confluence-esque links
# remove aspx
                link['href'] = link['href'].replace(".aspx", "");
# if copying directly into Confluence markdown entry, it needs to be different to using the SOAP converter
                if direct_confluence_entry:
# replace Sharepoint url
                    link['href'] = link['href'].replace(wiki_base_url, "/display/" + confluence_space_key + "/");
# pluses rather than %20s
                    link['href'] = link['href'].replace("%20", "+");
                else:
# remove Sharepoint url
                    link['href'] = link['href'].replace(wiki_base_url, "");
# spaces rather than %20s
                    link['href'] = link['href'].replace("%20", " ");
# remove aspx
                    link['href'] = link['href'].replace(".aspx", "");

# add Sharepoint url to any remaining sharepoint links
            else:
                link['href'] = sharepoint_url + link['href'];

# update relative image paths to point back to sharepoint
        images = innerDiv.find_all("img", src=re.compile("^\/"))
        if len(images) > 0:
            has_images.append(url)

            # it's not necessary for this to be within the if, but might as well
            for image in images:
                image['src'] = sharepoint_url + image['src']

# remove sharepoint layouts_data div content if exists (false,false,1 etc)
        layoutsData = innerDiv.find("span", id="layoutsData")
        if layoutsData != None:
            layoutsData.string = ""