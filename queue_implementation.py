from queue_self_made import Queue

class CustomerQueue:
    def __init__(self):
        self.line = Queue()
        self.customer_state = {}

    def enqueue_after(self, node, data): # New function for priority queue, seperated from queue because specific only to this implementation
        from node import Node
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def add_customer(self, name, state):
        self.customer_state[name] = state
        if state != "Regular":
            if not self.line.head or self.customer_state[self.line.head.data] == "Regular":
                self.line.enqueue_at_head(name)
            else:
                current = self.line.head
                while current.next and self.customer_state[current.next.data] != "Regular":
                    current = current.next
                self.enqueue_after(current, name)
        else:
            self.line.enqueue(name)

    def get_line(self):
        current = self.line.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result

    def serve_customer(self):
        returned_node = self.line.dequeue()
        if returned_node:
            self.customer_state.pop(returned_node.data, None)
            return returned_node.data
        return None
    
the_line = CustomerQueue()
while True:
    the_queue = the_line.get_line()
    if the_queue:
        print(the_queue)
    else:
        print("No one in line.")
    name = input("Please input name (or 'exit' to stop): ")
    if name.lower() == "exit":
        break

    state = input("Input customer State: ")
    if state.lower() != "regular":
        state = "Not Regular"
    else:
        state = "Regular"

    the_line.add_customer(name, state)

    the_queue = the_line.get_line()
    if the_queue:
        print(the_queue)
    else:
        print("No one in line.")

    serve = input("DO you wanna serve the next customer? (Y/N): ")
    while serve == "y":
        served = the_line.serve_customer()
        if served:
            print(f"Served customer: {served}")
        else:
            print("No customers in line.")
        print(the_line.get_line())
        serve = input("DO you wanna serve the next customer? (Y/N): ")
