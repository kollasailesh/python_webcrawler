__author__ = 'SAILESH'
import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.find_all('a', {'class': 'post-title'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    cleanWordlist(word_list)

def cleanWordlist(word_list):
    clean_Word_List = []
    for word in word_list:
        symbols = "!@#$%^&*()_+`~[]\;'./,\"<>?:"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word)>0:
            clean_Word_List.append(word)
    create_Dictionary(clean_Word_List)

def create_Dictionary(clean_Word_List):
    word_count = {}
    for word in clean_Word_List:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print(key, value)





start("https://www.thenewboston.com/forum/")
