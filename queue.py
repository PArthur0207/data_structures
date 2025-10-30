from node import Node
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head:
            ret_node = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return ret_node
        return None
    
    def is_empty(self):
        return self.head == None
        