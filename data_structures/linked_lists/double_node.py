class Node: 
    def __init__(self, data=None, next=None, prev=None): 
        self.data = data 
        self.next = next
        self.prev = prev


def push(head_ref, new_data):

    # 1 & 2: Allocate the Node & Put in the data
    new_node = Node(new_data)

    # 3. Make next of new node as head and previous as NULL
    new_node.next = head_ref
    new_node.prev = None

    # 4. change prev of head node to new node
    if head_ref is not None:
        head_ref.prev = new_node

    # 5. return new node as head
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
    print()


# Function to return elements in linked list as python list
def get_value_list(node): 
    values = []
    while (node != None): 
        values.append(node.data) 
        node = node.next

    return values


if __name__ == '__main__':

    ll = push_list(range(10))
    print_list(ll)

    h = ll
    while h is not None:
        prev = h.prev.data if h.prev is not None else ''
        next = h.next.data if h.next is not None else ''

        print('(', prev, ', ', h.data, ', ', next, ')')
        h = h.next
    
    print_list(ll)