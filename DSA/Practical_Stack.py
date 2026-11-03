class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, data):
        NewNode = Node(data)

        if self.isempty():
            self.top = NewNode
        else:
            NewNode.next = self.top
            self.top = NewNode

    def pop(self):
        if self.isempty():
            print("Stack is Underflow")
        else:
            curr = self.top
            print("Popped element:", curr.data)
            self.top = self.top.next
            curr = None

    def print_stack(self):
        curr = self.top

        while curr != None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def reverse(self):
        NewStack = stack()
        curr = self.top

        while curr:
            NewStack.push(curr.data)
            curr = curr.next

        NewStack.print_stack()

    def reverse_string(self, string):
        NewStack = stack()

        for ch in string:
            NewStack.push(ch)

        print("Reversed string: ", end="")

        while not NewStack.isempty():
            print(NewStack.top.data, end="")
            NewStack.top = NewStack.top.next
        print()


s = stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print("Original Stack:")
s.print_stack()

s.pop()

print("After Pop:")
s.print_stack()

print("Reversed Stack:")
s.reverse()

s.reverse_string("PYTHON")