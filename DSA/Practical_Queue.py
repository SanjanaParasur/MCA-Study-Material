class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        return self.front is None

    def enqueue(self, data):
        NewNode = Node(data)

        if self.isempty():
            self.front = NewNode
            self.rear = NewNode
        else:
            self.rear.next = NewNode
            self.rear = NewNode

    def dequeue(self):
        if self.isempty():
            print("Queue is Underflow")
        else:
            curr = self.front
            print("Deleted element:", curr.data)
            self.front = self.front.next
            curr = None

            if self.front is None:
                self.rear = None

    def print_queue(self):
        curr = self.front

        while curr != None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def reverse(self):
        NewStack = []

        curr = self.front

        while curr:
            NewStack.append(curr.data)
            curr = curr.next

        self.front = None
        self.rear = None

        while NewStack:
            self.enqueue(NewStack.pop())

    def merge(self, q2):
        curr = q2.front

        while curr:
            self.enqueue(curr.data)
            curr = curr.next

    def identical(self, q2):
        curr1 = self.front
        curr2 = q2.front

        while curr1 and curr2:
            if curr1.data != curr2.data:
                return False

            curr1 = curr1.next
            curr2 = curr2.next

        return curr1 is None and curr2 is None


q = queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

print("Original Queue:")
q.print_queue()

q.dequeue()

print("After Dequeue:")
q.print_queue()

q.reverse()

print("Reversed Queue:")
q.print_queue()


q2 = queue()
q2.enqueue(60)
q2.enqueue(70)

q.merge(q2)

print("Merged Queue:")
q.print_queue()


q3 = queue()
q3.enqueue(10)
q3.enqueue(20)
q3.enqueue(30)
q3.enqueue(40)

q4 = queue()
q4.enqueue(10)
q4.enqueue(20)
q4.enqueue(30)
q4.enqueue(40)

if q3.identical(q4):
    print("Queues are Identical")
else:
    print("Queues are Not Identical")