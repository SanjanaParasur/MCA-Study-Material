#syntax
#class MyCustomException(Exception):
#    pass


class InvalidAgeError(Exception):
    pass

try:
    age=int(input("Enter Age :"))
    if age < 18:
        raise InvalidAgeError("You must be 18 or above")
    print("Eligible")
except InvalidAgeError as e:
    print("Error :", e)

print("Program completed")
