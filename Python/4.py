#Accept two values S and N .Print Square of first N numbers starting from S
S = int(input("Enter starting number S: "))
N = int(input("Enter count N: "))

for i in range(S, S+N):
    print(i ** 2)