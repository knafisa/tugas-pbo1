while True:
    try:
        number = int(input("enter an int number: "))
        print(5/number)
        break
    except ValueError:
        print("wrong value")
    except ZeroDivisionError:
        print("sorry. i cannot divide by zero")
    except:
        print("i don't know what to do...")