import random
import urllib.request

def web_image(url):
    name = random.randrange(1, 1000)
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullname)

web_image("https://a2.muscache.com/ic/pictures/65125975/3f492bb3_original.jpg")