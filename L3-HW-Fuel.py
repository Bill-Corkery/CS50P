while True:
    try:
        number1,number2 = input("Fraction: ").split("/")
        number1 = int(number1)
        number2 = int(number2)
        fuel = int(round((number1 / number2)*100))
        if fuel <= 100:
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
if fuel >= 99:
   print("F")
elif fuel <= 1:
    print("E")
else:
    print (str(fuel)+"%")