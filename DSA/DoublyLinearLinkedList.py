class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at the end
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    # Insert node at a given position
    def insert(self, value, position):
        new_node = Node(value)

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node
            return

        temp = self.head

        for i in range(position - 2):
            if temp is None:
                print("Invalid position")
                return

            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

    def search_count(self, value):
        temp = self.head
        count = 0

        while temp is not None:
            if temp.data == value:
                count += 1

            temp = temp.next

        if count > 0:
            print("Number found:", value)
            print("Occurrence:", count)
        else:
            print("Number not found")

    # Delete a node by value
    def delete(self, value):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        # If the first node contains the value
        if temp.data == value:
            self.head = temp.next

            if self.head is not None:
                self.head.prev = None

            return

        # Search for the value
        while temp is not None and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        # Connect previous and next nodes
        temp.prev.next = temp.next

        if temp.next is not None:
            temp.next.prev = temp.prev

    # Display the linked list
    def print(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    def printrev(self):
        temp = self.head

        print("Reverse Linked List:")
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data, end=" ")
            temp=temp.prev
        print()



# Main program
list1 = LinkedList()

list1.append(10)
list1.append(20)
list1.append(30)
list1.insert(25, 3)

print("Original Linked List:")
list1.print()

list1.delete(20)

print("After deleting 20:")
list1.print()

list1.printrev()

num = int(input("Enter number to search: "))
list1.search_count(num)
