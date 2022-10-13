# single linked node

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

# UTILITY FUNCTIONS 
# Function to insert a node at the 
# beginning of the linked list 
def push(head_ref, new_data):

    new_node = Node(new_data)
    new_node.next = head_ref

    return new_node

# utility function to push a list of elements
def push_list(A):
    head = None

    for i in A:
        head = push(head, i)

    return head

# Function to print nodes in a given linked list 
def print_list(node): 
    while (node != None): 
        print(node.data, end = " ") 
        node = node.next


# Function to return elements in linked list as python list
def get_value_list(node): 
    values = []
    while (node != None): 
        values.append(node.data) 
        node = node.next

    return values