num = int(input("Enter a number: "))
p = len(str(num))
total = 0
n = num
while num > 0:
     total += (num % 10) ** p
     num //= 10
if n == total:
     print("is Armstrong number")
else:
     print("is not an Armstrong number")

