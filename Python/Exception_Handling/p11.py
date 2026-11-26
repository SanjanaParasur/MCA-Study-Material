try:
    a = int("10")
    b = int("hello")
    c = 10 / 2
except ZeroDivisionError:
    print("Zero")
except ValueError:
    print("Value")
else:
    print("Else")
finally:
    print("Finally")
print("End")