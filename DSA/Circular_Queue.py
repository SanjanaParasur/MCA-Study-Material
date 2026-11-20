#Linear Queue using linkedlist
class Node:
    def __init__(self, value):

        self.data=value 
        self.next=None

class CQueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self, new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
        self.rear.next=self.front  #added for circular

    def dequeue(self):
        if self.front:
            temp=self.front
            if self.front==self.rear: #updated for circular queue
                self.rear=self.rear=None
                print("Now queue is empty")
            else:
                self.front=self.front.next
                self.rear.next=self.front #added for circular 
            temp=None
        else:
            print("Queue is empty")

    def print(self):
        temp=self.front
        while True:
            print(temp.data,end=" ")
            temp=temp.next
            if temp==self.front:
                break
        print()

cu=CQueue()
cu.enqueue(Node(10))
cu.enqueue(Node(20))
cu.enqueue(Node(300))
cu.enqueue(Node(40))
cu.enqueue(Node(100))
cu.print()
cu.dequeue()
cu.print()
cu.dequeue()
cu.print()
cu.dequeue()
cu.print()
cu.dequeue()
cu.print()

