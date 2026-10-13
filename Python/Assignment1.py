#1. Write a program to read a file and count how many vowels are present in its content

f = open(r"D:\MCA-Study-Material-Clone\MCA-Study-Material\Python\sample.txt", "r")
data = f.read()

count = 0

for ch in data:
    if ch.lower() in "aeiou":
        count += 1

f.close()

print("Total vowels:", count)


# 2.Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line.
f = open(r"D:\MCA-Study-Material-Clone\MCA-Study-Material\Python\sample.txt", "r")
lines = f.readlines()

print("Total lines:", len(lines))
print("2nd line:", lines[1])
print("4th line:", lines[3])

f.close()

#3. Take a sentence from the user, split it into words, and store them in a list. Print the longest word.
sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
print("Longest word:", longest_word)


#Read a file,split its content into words, and store them in a list.
#1.Print the total number of words
#2.Print all unique words

f = open(r"D:\MCA-Study-Material-Clone\MCA-Study-Material\Python\sample.txt", "r")
content = f.read()
words = content.split()
f.close()

print("Total words:", len(words))
print("Unique words:", set(words))
