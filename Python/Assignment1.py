#1. Write a program to read a file and count how many vowels are present in its content

f = open("sample.txt", "r")
data = f.read()

count = 0

for ch in data:
    if ch.lower() in "aeiou":
        count += 1

f.close()

print("Total vowels:", count)