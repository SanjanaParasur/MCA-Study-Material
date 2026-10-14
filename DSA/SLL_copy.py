
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    # Append a node
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    # Insert a node at a given position
    def insert(self, new_node, pos):
        if pos == 1:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
                new_node.next = self.head
                self.head = new_node
                temp.next=self.head
            else:
                p=1
                temp=self.head
                while(p!=pos-1):
                    temp=temp.next
                    p+=1
                new_node.next=self.head
                temp.next=self.head
        
        else:
            p = 1
            temp = self.head

            while p < pos - 1 and temp.next != self.head:
                temp = temp.next
                p += 1

            if p != pos - 1:
                print("Invalid position")
                return

            new_node.next = temp.next
            temp.next = new_node


    # Delete a node by value
    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        prev = None

        # If the first node contains the value
        if temp.data == value:
            # Only one node
            if temp.next == self.head:
                self.head = None
            else:
                last = self.head

                while last.next != self.head:
                    last = last.next

                self.head = self.head.next
                last.next = self.head

            return

        prev = temp
        temp = temp.next

        while temp != self.head and temp.data != value:
            prev = temp
            temp = temp.next

        if temp == self.head:
            print("Value not found")
            return

        prev.next = temp.next
        temp = None

    # Display the linked list
    def Print(self):
        print()
        print("List elements:")

        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" ")
            temp = temp.next

            if temp == self.head:
                break

        print()


# Main program
list1 = SLL()

list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))

print("Original Linked List:")
list1.Print()

list1.insert(Node(34), 4)
print("After Insertion:")
list1.Print()

#list1.delete(30)

#print("After Deletion:")
#list1.Print()
