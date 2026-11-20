
# Stack using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            temp = self.top
            popped_data = temp.data
            self.top = self.top.next
            temp.next = None
            return popped_data

    def is_empty(self):
        return self.top is None

    def print(self):
        temp = self.top
        print("Stack elements...")
        while temp:
            print(temp.data)
            temp = temp.next


# Linear Queue using Linked List

class LQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self):
        if self.front:
            temp = self.front
            dequeued_data = temp.data
            self.front = self.front.next

            if self.front is None:
                self.rear = None

            temp.next = None
            return dequeued_data
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        return self.front is None

    def print(self):
        temp = self.front
        print("Queue elements...")
        while temp:
            print(temp.data)
            temp = temp.next
        print()


# Reverse Queue using Stack

def reverse_queue(q1):
    st1 = Stack()

    while not q1.is_empty():
        st1.push(Node(q1.dequeue()))

    st1.print()


# Reverse Stack using Queue

def reverse_stack(s1):
    q1 = LQueue()

    while not s1.is_empty():
        q1.enqueue(Node(s1.pop()))

    q1.print()


# Main Program

que = LQueue()
stk1 = Stack()

que.enqueue(Node(10))
que.enqueue(Node(20))
que.enqueue(Node(300))
que.enqueue(Node(40))
que.enqueue(Node(100))

que.print()
reverse_queue(que)


stk1.push(Node(100))
stk1.push(Node(50))
stk1.push(Node(200))
stk1.push(Node(400))

stk1.print()
reverse_stack(stk1)
