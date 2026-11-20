# Write a program to accept N integers into array and calculate and display the sum of all the elements in the array.
n= int(input("Enter the number of elements in the array: "))
arr= []
for i in range(n):
    num = int(input(f"Enter element : "))
    arr.append(num)
    total = 0
    for num in arr:
        total = total + num
print("The sum of all the elements in the array is:", total)