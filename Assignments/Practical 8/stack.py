class node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def push(head, data):
    new_node = node(data, head)
    head = new_node
    return head

def pop(head):
    if head is None:
        return None
    data = head.data
    head = head.next
    return data, head

def traverse(head):
    while head is not None:
        print(head.data)
        head = head.next

head = node(1, None) # Create a node with data 1
head = push(head, 2) # Push 2 onto the stack
head = push(head, 3) # Push 3 onto the stack
head = push(head, 4) # Push 4 onto the stack
data, head = pop(head) # Pop the stack
traverse(head) # Print the stack

# Github Repo Link: https://github.com/s-shubham-22/20CE123_CE259_PIP