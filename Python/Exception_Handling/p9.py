class InsufficientBalance(Exception):
    pass

balance=5000
withdrawal=7000

try:
    if withdrawal > balance:
        raise InsufficientBalance("Insufficient Bank balance")

    balance=balance-withdrawal
    print("Withdrawal Succesful")
    print("Remaining balance :", balance)

except InsufficientBalance as e:
    print("Transition failed :",e)

finally:
    print("Thankyou for using bank")
