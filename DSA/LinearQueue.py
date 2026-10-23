#Linear Queue using linkedlist
class Node:
    def __init__(self, value):

        self.data=value 
        self.next=None

class LQueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self, new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node

    def dequeue(self):
        if self.front:
            temp=self.front
            self.front=self.front.next
            if self.front==None:
                self.rear=None
                print("Now queue is empty")
            temp=None
        else:
            print("Queue is empty")



    def print(self):
        temp=self.front
        while temp:
            print(temp.data)
            temp=temp.next
        print()

qu=LQueue()
qu.enqueue(Node(10))
qu.enqueue(Node(20))
qu.enqueue(Node(300))
qu.enqueue(Node(40))
qu.enqueue(Node(100))
qu.print()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.print()
qu.dequeue()
qu.enqueue(Node(90))
qu.enqueue(Node(50))
qu.print()

