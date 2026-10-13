#1. Write a program to read a file and count how many vowels are present in its content

f = open(r"D:\MCA-Study-Material-Clone\MCA-Study-Material\Python\sample.txt", "r")
data = f.read()

count = 0

for ch in data:
    if ch.lower() in "aeiou":
        count += 1

f.close()

print("Total vowels:", count)


# Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line.
f = open(r"D:\MCA-Study-Material-Clone\MCA-Study-Material\Python\sample.txt", "r")
lines = f.readlines()
f.close()

print("Total lines:", len(lines))
print("2nd line:", lines[1] if len(lines) > 1 else "Does not exist")
print("4th line:", lines[3] if len(lines) > 3 else "Does not exist")
