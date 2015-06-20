__author__ = 'SAILESH'
# As there is no implicit function to sort a dictionary it is easy to sort by converting it into a zip and manipulating it.
Stocks = {
    'AMZN': 306.54,
    'GOOG':  560.98,
    "apple": 99.28
}

print(min(zip(Stocks.values(), Stocks.keys())))
print(max(zip(Stocks.values(), Stocks.keys())))
print(sorted(zip(Stocks.values(), Stocks.keys())))