#Search an element in an array and display the index of the element if found, otherwise display a message that the element is not found.
n = int(input("Enter number of elements in array: "))
arr= []

for i in range (n):
    num = int(input(f"Enter element :"))
    arr.append(num)
    
x = int(input("Enter the element to search: "))
found = False

for i in range(n):
    if arr[i] == x:
        print(f"Element found at index {i}")
        found = True
        break
if not found:
    print("Element not found")