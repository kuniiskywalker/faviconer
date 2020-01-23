from urllib import parse
import requests
from bs4 import BeautifulSoup

def get_by_url(url):
    """get favicon url"""
    r = requests.get(url)
    html = r.text

    print("this is text")
    print(html)


    if html:
        target = get_by_html(r.text)
        if target:
            return target
    return get_default(url)

def get_default(url):
    """get favicon by url"""
    target = get_url(url)
    return '{target}favicon.ico'.format(target=target)

def get_by_html(html):
    """get favicon by html"""
    soup = BeautifulSoup(html, 'html.parser')
    node = soup.find('link', attrs={'rel': 'icon'})
    if node:
        return node.get('href')
    return ''

def get_url(url):
    """get scheme and domain"""
    return '{uri.scheme}://{uri.netloc}/'.format(uri=parse.urlparse(url))
