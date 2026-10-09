#Count even and odd numbers
n=int(input("Enter number of elements in array:"))
arr=[]
for i in range (n):
    num=int (input(f"Enter elements:"))
    arr.append(num)
    even_count=0
    odd_count=0
    for num in arr:
        if num % 2 == 0 :
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
print("The number of even numbers in array is :",even_count)
print("The number of odd numbers in array is :",odd_count)


            