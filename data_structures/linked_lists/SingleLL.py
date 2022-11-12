# single linked node

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None


class LinkedList:

    def __init__(self, data=None):
        if data is None:
            self.head = data
            self.N = 0        # length of list
        else:
            self.head = Node(data)
            self.N = 1


    def is_empty(self):
        return self.head is None


    def push(self, data):
        '''
        add data to front of list
        ''' 

        # 1) create new node
        new_node = Node(data)

        # 2) assign previous head a next to new node
        new_node.next = self.head

        # 3) make new node the head
        self.head = new_node

        # 4) update length of linked list
        self.N += 1

    
    def peek(self):
        '''
        return value of head
        '''
        return self.head.data


    def pop(self):
        '''
        remove head and return value of head
        '''
        if self.is_empty():
            raise ValueError('Linked list is empty')

        # 1) retrieve value of head
        value = self.head.data

        # 2) remove head 
        self.head = self.head.next

        # 3) update length 
        self.N -= 1

        return value


    def insert_end(self, data):
        '''
        insert at end of list
        '''
        new_node = Node(data)

        # 1) iterate til get to end of list
        node = self.head
        while node.next is not None:
            node = node.next 

        # 2) add new node to end
        node.next = new_node
        

    def insert_after(self, node, data):
        '''
        insert after given node in list
        '''
        # 1) create a new node
        new_node = Node(data)

        # 2) assign next of new node as next of previous node
        new_node.next = node.next 

        # 3) make previous node's next new_node
        node.next = new_node


    def delete(self, key):
        '''
        delete node where key is data of node
        '''
        # get head pointer
        node = self.head

        # check if list is empty
        if node is None:
            raise TypeError('List is empty')

        # check if deleting head
        if node.data == key:
            self.head = self.head.next
            return

        # keep track of previous node since will need it for linking with delete node's next
        prev = node 
        node = node.next 

        # loop through rest of list
        while node is not None:
            # found node
            if node.data == key:
                break
            # iterate nodes
            prev = node 
            node = node.next
        
        # if key not in list
        if node is None:
            return

        # delete node
        prev.next = node.next



    # implement iterator for linked list 
    def __iter__(self):
            self.current_head = self.head
            return self

    def __next__(self):

        if  self.current_head is not None:
            val = self.current_head.data
            self.current_head = self.current_head.next
            return val

        raise StopIteration

    # return length of list
    def __len__(self):
        return self.N

    # def __str__(self):
    #     return '->'.join([i for i in self.__next__])

def print_linked_list(LL):
    elements = [str(i) for i in LL]
    elements.append('NULL')
    s = ' -> '.join(elements)
    print(s)

if __name__ == '__main__':

    values = [1, 2, 3, 4, 5]

    # instantiate linked list
    LL = LinkedList()

    # test is_empty()
    result, ans = LL.is_empty(), True
    assert result == ans, f'Error: push() should return {ans} but returned {result}'

    # test __len__()
    result, ans = len(LL), 0
    assert result == ans, f'Error: push() should return {ans} but returned {result}'

    # add values to linked list
    for i in values:
        LL.push(i)

    # test is_empty()
    result, ans = LL.is_empty(), False
    assert result == ans, f'Error: push() should return {ans} but returned {result}'
    
    # test __len__()
    result, ans = len(LL), len(values)
    assert result == ans, f'Error: push() should return {ans} but returned {result}'

    # test push()
    result = [i for i in LL]
    ans_list = [5, 4, 3, 2, 1]
    assert result == ans_list, f'Error: push() should return {ans_list} but returned {result}'
    
    # test peak()
    result, ans = LL.peek(), ans_list[0]
    assert result == ans, f'Error: peek() should return {ans} but returned {result}'

    # test pop()
    for i in range(len(ans_list)):
        result, ans = LL.pop(), ans_list[i]
        assert result == ans, f'Error: pop() should return {ans} but returned {result}'

    # add values to linked list
    for i in values:
        LL.push(i)
    
    # test insert()
    num = 1000
    LL.insert_end(num)
    result = [i for i in LL]
    ans_list.append(num)
    assert result == ans_list, f'Error: insert_end() should return {ans_list} but returned {result}'

    # get 4th of node list
    i, node = 1, LL.head
    while i < 4:
        node = node.next
        i += 1
    print('4th node:', node.data)

    result, ans = node.data, 2
    assert result == ans, f'Error: insert_after() should return {ans} but returned {result}'
    
    num = 15
    LL.insert_after(node, num)
    result = [i for i in LL]
    ans_list.insert(4, num)
    assert result == ans_list, f'Error: insert_after() should return {ans_list} but returned {result}'


    for i in LL:
        print(i)



    # deleter from front
    num = 5
    LL.delete(num)
    result = [i for i in LL]
    ans_list.pop(0)
    assert result == ans_list, f'Error: delete() should return {ans_list} but returned {result}'

    # deleter from end
    num = 1000
    LL.delete(num)
    result = [i for i in LL]
    ans_list.pop()
    assert result == ans_list, f'Error: delete() should return {ans_list} but returned {result}'

    # deleter from middle
    num = 2
    LL.delete(num)
    result = [i for i in LL]
    ans_list.pop(2)
    assert result == ans_list, f'Error: delete() should return {ans_list} but returned {result}'

    print_linked_list(LL)
