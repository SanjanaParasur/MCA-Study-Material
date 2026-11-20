n = int(input("Enter number of elements in array:"))
arr = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

for i in range (n-1 ,-1, -1):
    print(arr[i], end=" ")
    