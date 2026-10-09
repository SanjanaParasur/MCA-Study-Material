#Find the smallest and largets element
n=int(input("Enter number of elements in array:"))
arr=[]
for i in range (n):
    num=int(input(f"Enter element :"))
    arr.append(num)
arr.sort()
print("Smallest number:",arr[0])
print("Second Smallest Number:",arr[1])
print("Largest number:",arr[-1])
print("Second Largest Number:",arr[-2])