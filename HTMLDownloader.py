import requests, os, re
from bs4 import BeautifulSoup

urls = list()

def getUrls(href, url):
    
    if not href.endswith('.html'):
        href = href + '.html'
    if not url.endswith('/'):
        url = url + '/'
    
    regexp = re.compile(r'(http)(s?)://(.*?)/')
    urlpart = regexp.search(url).group()
    res = requests.get(url)
    
    # Catching Exceptions
    try:
        res.raise_for_status()
    except Exception as e:
        print('Problem: %s'%(e))
        
    # Saving file in the hard-drive
    file = open(href,'wb')
    for chunk in res.iter_content(100000):
        file.write(chunk)
    file.close()

    # Parsing and getting urls from the page
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href != None and (re.search(r'^(http|mailto:|.)',href) or href.startswith(urlpart))==None:
            if href.startswith('/'):
                url = urlpart + href[1:]
            else:
                url = urlpart + href
            if not url in urls:
                urls.append(url)
                getUrls(href, url)
# Calling the function to get urls from a web page to download content in it
getUrls('toc', 'https://automatetheboringstuff.com')
