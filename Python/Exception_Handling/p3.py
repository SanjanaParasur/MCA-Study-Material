try:
    print("Step1")
    a=int("hello")
    print("Step2")
    b=10/0
    print("step3")
except ValueError:
    print("Value Error occured")
except ZeroDivisionError:
    print("Zero division error occured")

print("Program ended")