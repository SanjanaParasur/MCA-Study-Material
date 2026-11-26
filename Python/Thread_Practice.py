import threading 
import time

def greet():
    time.sleep(3)
    print("Hello")

def greet1():

    print("World")

def greet2():
    print("Sanjana")

t1 = threading.Thread(target=greet)
t2 = threading.Thread(target=greet1)
t3 = threading.Thread(target=greet2)


t1.start()
t1.join()
t2.start()
t3.start()

