__author__ = 'SAILESH'
import requests
from bs4 import BeautifulSoup

def trade_spider(max_size):
    page = 2
    while page <= max_size:
        print("In while loop", page)
        url = "https://www.thenewboston.com/forum/home.php?page=3"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'post-title'}):
            href = link.get('href')
            print(href)
        page = page + 10
trade_spider(2)
