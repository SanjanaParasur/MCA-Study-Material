n = int(input("Enter number of elements in array:"))
arr = []
for i in range (n):
    num = int(input("Enter element :"))
    arr.append(num)

new_arr=[]
for i in arr:
   if i != new_arr:
       new_arr.append(i)
print("Array after removing duplicate elements:",new_arr)

