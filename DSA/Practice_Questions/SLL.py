
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            p = 1

            while p < pos - 1 and temp is not None:
                temp = temp.next
                p += 1

            if temp is None:
                print("Invalid position")
                return

            new_node.next = temp.next
            temp.next = new_node

    def delete(self, value):
        temp = self.head
        prev = None
        if temp.data == value:
            self.head = self.head.next
        else:
            while(temp.data != value and temp.next != None):
                prev = temp
                temp = temp.next
                if temp == None:
                    print("Value not found")
                    return
            prev.next = temp.next
            temp = None

    def Print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


list1 = SLL()

list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))

print("Original Linked List:")
list1.Print()

list1.insert(Node(34), 1)

print("After Insertion:")
list1.Print()

list1.delete(30)
list1.Print()
