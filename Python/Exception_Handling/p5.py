try:
    num=int(input("Enter Number :"))
    result=100/num
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Zero division error occured")
else:
    print(result)
finally:
    print("Program execution completed")