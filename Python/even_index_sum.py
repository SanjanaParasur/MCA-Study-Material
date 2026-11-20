# even index sum
def even_index_sum(lst):
    sum = 0
    for i in range(0, len(lst), 2):
        sum += lst[i]
    return sum

a = [10, 20, 30, 40, 50, 60]
print(even_index_sum(a))

#for i in range (len(a)):
#    if i % 2 == 0:
#        sum += a[i]
#print(sum

