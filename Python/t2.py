import threading

def add(a,b):
    print("Sum :",a-b)

t1=threading.Thread(target=add, args=(30,40))
t1.start()
