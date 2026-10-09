#accept sentence from user and count the vowels
sen=input("Enter a sentence: ")
a = e = i = o = u = 0
count = 0   
for char in sen:
    if char == 'a' or char == 'A':
        a += 1
    elif char == 'e' or char == 'E':
        e += 1
    elif char == 'i' or char == 'I':
        i += 1
    elif char == 'o' or char == 'O':
        o += 1
    elif char == 'u' or char == 'U':
        u += 1
print("A or a:", a)
print("E or e:", e)
print("I or i:", i)
print("O or o:", o)
print("U or u:", u)