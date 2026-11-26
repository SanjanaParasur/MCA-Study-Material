try:
    num1=int(input("Enter first number :"))
    num2=int(input("Enter second number :"))
    result=num1/num2
    print("Division :",result)
except ValueError:
    print("Please enter valid integers")
except ZeroDivisionError:
    print("Second number cannot be zero")
else:
    print("Calculation successful")
finally:
    print("Program execution completed")