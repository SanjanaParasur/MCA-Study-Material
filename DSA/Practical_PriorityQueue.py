class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None

    # 1. Add process according to priority

    def enqueue(self, pid, name, priority):
        new_node = Node(pid, name, priority)
        # If queue is empty or new process has higher priority
        if self.front == None or priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front
            # Find correct position according to priority
            while temp.next != None and temp.next.priority <= priority:
                temp = temp.next
            # Insert the new process
            new_node.next = temp.next
            temp.next = new_node

        print("Process Added")


    # 2. Execute highest priority process
    def dequeue(self):
        if self.front == None:
            print("Queue is Empty")
        else:
            temp = self.front
            print("Executed Process:", temp.pid, temp.name)
            self.front = self.front.next
    
    
    # 3. Display next process
    def display_next(self):
        if self.front == None:
            print("Queue is Empty")
        else:
            print("Next Process:", self.front.pid, self.front.name,
                  "Priority:", self.front.priority)
    
    
    # 4. Display all processes
    def display_all(self):
        if self.front == None:
            print("Queue is Empty")
        else:
            temp = self.front
            while temp != None:
                print(temp.pid, temp.name, "Priority:", temp.priority)
                temp = temp.next
    
    
    # 5. Count total processes
    def count(self):
        temp = self.front
        c = 0
        while temp != None:
            c = c + 1
            temp = temp.next
        print("Total Processes:", c)

# Main Program
pq = PriorityQueue()
pq.enqueue(101, "System", 1)
pq.enqueue(102, "Interactive", 2)
pq.enqueue(103, "Background", 3)
pq.enqueue(104, "Low Priority", 4)
print("\nAll Processes:")
pq.display_all()
print("\nNext Process:")
pq.display_next()
print("\nCount:")
pq.count()
print("\nExecute Process:")
pq.dequeue()
print("\nRemaining Processes:")
pq.display_all()
print("\nCount:")
pq.count()