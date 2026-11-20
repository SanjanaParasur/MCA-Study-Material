class node:
    def __init__(self,value, pr):
        self.data=value
        self.priority=pr
        self.next=None

class priorityQueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self, new_node):
        # for front or 1st position
        if self.front==None:   #first node to be inserted
            self.front=new_node
            return
        if self.front.priority > new_node.priority:
            new_node.next=self.front
            self.front=new_node
            return
        else:
            temp=self.front
            while temp:
                if new_node.priority<=temp.priority:
                    break
                else:
                    prev=temp
                    temp=temp.next
            prev.next=new_node
            new_node.next=temp
    def dequeue(self):
        if self.front:
            temp=self.front
            print("Node Deleted: ",temp.data)
            self.front=self.front.next
        else:
            print("Queue is Empty")

    def display(self):
        temp=self.front
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()

        #create priority queue
pq=priorityQueue()
pq.enqueue(node(100,2))
pq.enqueue(node(500,5))
pq.enqueue(node(300,3))
pq.enqueue(node(600,1))
pq.enqueue(node(800,8))

pq.display()

pq.dequeue()
pq.dequeue()
pq.display()