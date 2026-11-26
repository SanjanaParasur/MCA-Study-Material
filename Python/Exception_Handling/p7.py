age=18
try:
    if age < 18:
        raise ValueError("You must be 18 or above")
    print("Eligible")
except ValueError as e:
    print("Error :",e)

print("Program completed")
