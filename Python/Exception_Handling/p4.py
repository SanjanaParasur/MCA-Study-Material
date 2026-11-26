try:
    a=int(input("enter number"))
    result=100/a
except ValueError:
    print("Value Error occuredd")
except ZeroDivisionError:
    print("Zero division error occured")
else:
    print("Result=",result)
    print("Program completed succesfully")