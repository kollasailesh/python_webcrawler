__author__ = 'SAILESH'

def pizza():
    print("Functions are cool")

def bitcoin_to_dollar(btc=1):
    amount = btc * 527
    return amount

bitcoin_Value= bitcoin_to_dollar()
print(bitcoin_Value)

def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(3, 40, 54)
add_numbers(89,990)