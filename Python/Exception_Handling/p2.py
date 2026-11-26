try:
    a=int(input("Enter number :"))
    result=100/a
    print(result)
except ValueError:
    print("Enter valid number")

except ZeroDivisionError:
    print("You cannot divide by zero")