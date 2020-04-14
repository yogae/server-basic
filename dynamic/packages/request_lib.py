from bs4 import BeautifulSoup
import requests

def get_title(uri):        
    response = requests.get(uri)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        return soup.title.name
    else:
        raise Exception('error')