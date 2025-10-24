from linked_list import LinkedList

ll = LinkedList()

operators_used = ["-", "+", "=", "/", "^", "*", "(", ")"]
values = {
"^": 3,
"*": 2,
"/": 2,
"+": 1,
"-": 1,
"(": 0,
")": 0
}
original_operation = "(A + B) * C"
output = ""

operation = original_operation.replace(" ", "")

for item in operation:
    if item in operators_used:
        if item == "(":
            ll.insert_at_beginning(item)

        elif item == ")":
            while ll.head and ll.head.data != "(":
                output += ll.remove_at_beginning()

            if ll.head and ll.head.data == "(":
                ll.remove_at_beginning()
            
        else:
            while ll.head and ll.head.data != "(" and values[item] <= values[ll.head.data]:
                output += ll.remove_at_beginning()
            
            ll.insert_at_beginning(item)
        
    else:
        output += item

while ll.head:
    output += ll.remove_at_beginning()

print(f"Infix: {original_operation} \nPostfix: {output}")