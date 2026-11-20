class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Create linked list
    def create(self, values):
        for value in values:
            self.insert_end(value)

    # Insert node at the end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Traverse and print nodes
    def traverse(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    # Insert node at a specific position (1-based)
    def insert_position(self, data, position):
        new_node = Node(data)

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for _ in range(position - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Find middle node
    def find_middle(self):
        slow = self.head
        fast = self.head

        if self.head is None:
            print("List is empty")
            return

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:", slow.data)

    # Delete node at a specific position (1-based)
    def delete_node(self, position):
        if self.head is None or position < 1:
            print("Invalid position")
            return

        if position == 1:
            self.head = self.head.next
            return

        temp = self.head

        for _ in range(position - 2):
            if temp.next is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next

    # Reverse linked list
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    # Sum every two consecutive node values
    def consecutive_sums(self):
        temp = self.head

        while temp and temp.next:
            print(temp.data + temp.next.data, end=" ")
            temp = temp.next

        print()


# Main program
SSL = SinglyLinkedList()

n = int(input("Enter number of nodes: "))
values = list(map(int, input("Enter node values: ").split()))

SSL.create(values)

print("Linked List:")
SSL.traverse()

data = int(input("Enter value to insert: "))
position = int(input("Enter insertion position: "))
SSL.insert_position(data, position)
print("After insertion:")
SSL.traverse()

SSL.find_middle()

position = int(input("Enter position to delete: "))
SSL.delete_node(position)
print("After deletion:")
SSL.traverse()

SSL.reverse()
print("Reversed Linked List:")
SSL.traverse()

print("Sums of consecutive nodes:")
SSL.consecutive_sums()