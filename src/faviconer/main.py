from urllib import parse
import requests
from bs4 import BeautifulSoup

def get_favicon(url):
    """get favicon url"""
    r = requests.get(url)
    html = r.text
    if html:
        return get_favicon_by_html(r.text)
    return get_favicon_by_url(url)

def get_url(url):
    """get scheme and domain"""
    return '{uri.scheme}://{uri.netloc}/'.format(uri=parse.urlparse(url))

def get_favicon_by_url(url):
    """get favicon by url"""
    target = get_url(url)
    return '{target}favicon.ico'.format(target=target)

def get_favicon_by_html(html):
    """get favicon by html"""
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find('link', attrs={'rel': 'icon'}).get('href')
