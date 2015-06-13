__author__ = 'SAILESH'

while True:
    try:
        tuna = int(input("What's your Fav Number?"))
        print(18/tuna)
        break
    except ValueError:
        print("Make sure and enter a number")
    except ZeroDivisionError:
        print("Pick anything except Zero")
    except:
        break
    finally:
        print("Execute this no matter what")