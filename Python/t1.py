import threading
import time

counter=0
def counting():
    global counter
    for _ in range(100000):
        counter += 1
    print(counter)

t1=threading.Thread(target=counting)
t2=threading.Thread(target=counting)

t1.start()
print("after t1 :",counter)
t2.start()

