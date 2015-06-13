__author__ = 'SAILESH'
from urllib import request

goog_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=4&e=21&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv"

def download_file(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r"goog_url"
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()
download_file(goog_url)

