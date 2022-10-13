from data_structures.linked_lists.node import Node

class LinkedListQueue:

    def __init__(self):
        
        self.head, self.tail = None, None


    def is_empty(self):
        return self.head is None 


    def peek(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        else:
            return self.head.data


    def push(self, value):
        t = Node(value)
        if self.tail is not None:
            self.tail.next = t; 

        self.tail = t
        if self.head is None:
            self.head = self.tail
        

    def pop(self):
        if self.is_empty():
            raise ValueError('Queue is empty')

        value = self.head.data

        self.head = self.head.next

        if self.head is None:
            self.last = None
        
        return value
 

    def __iter__(self):
            self.currenthead = self.head
            return self

    def __next__(self):

        if  self.currenthead is not None:
            val = self.currenthead.data 
            self.currenthead = self.currenthead.next
            return val

        raise StopIteration


if __name__ == '__main__':
    values = [10, 5, 100, 2]


    q = LinkedListQueue()
    for i in values:
        q.push(i)

    result, ans = q.peek(), 10
    assert result == ans, f'Error: peek() should return {ans} but returned {result}'

    result, ans = q.is_empty(), False
    assert result == ans, f'Error: is_empty() should return {ans} but returned {result}'

    result = [i for i in q]
    ans_stack = values
    assert result == ans_stack, f'Error: Order of values should be {ans_stack} but returned {result}'

    for ans in ans_stack:
        result = q.pop()
        assert result == ans, f'Error: pop() should return {ans} but returned {result}'

    result, ans = q.is_empty(), True
    assert result == ans, f'Error: is_empty() should return {ans} but returned {result}'

    # should throw ValueError
    # q.pop()