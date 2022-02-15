try:
    value = int(input("enter a value:"))
    print(value/value)
except ValueError:
    print("bad input...")
except ZeroDivisionError:
    print("very bad input...")
except:
    print("booo!")