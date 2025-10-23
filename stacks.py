from linked_list import LinkedList

ll = LinkedList()

operators = ["-", "+", "=", "/", "^", "*", "(", ")"]

operation = "(A + B) * C"
output = ""

for item in operation:
    if item in operators:
        ll.insert_at_end(item)
    else:
        output = output + item

print(output + str(ll.use_list()))