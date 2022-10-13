from data_structures.linked_lists.node import Node

class LinkedListStack:

    def __init__(self):
        self.top : Node = None


    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            return self.top.data

    def push(self, value):
        if self.is_empty():
            self.top = Node(value)
        else:
            t = Node(value)    # make new Node for new head
            t.next = self.top  # append previous list to new head
            self.top = t       # assign new top

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            val = self.top.data       # get data of head
            self.top = self.top.next  # remove head

            return val

    def __iter__(self):
            self.current_top = self.top
            return self

    def __next__(self):

        if  self.current_top is not None:
            val = self.current_top.data
            self.current_top = self.current_top.next
            return val

        raise StopIteration


if __name__ == '__main__':
    values = [10, 5, 100, 2]

    s = LinkedListStack()
    for i in values:
        s.push(i)

    result, ans = s.peek(), 2
    assert result == ans, f'Error: peek() should return {ans} but returned {result}'

    result, ans = s.is_empty(), False
    assert result == ans, f'Error: is_empty() should return {ans} but returned {result}'

    result = [i for i in s]
    ans_stack = [2, 100, 5, 10]
    assert result == ans_stack, f'Error: Order of values should be {ans_stack} but returned {result}'

    for ans in ans_stack:
        result = s.pop()
        assert result == ans, f'Error: pop() should return {ans} but returned {result}'

    result, ans = s.is_empty(), True
    assert result == ans, f'Error: is_empty() should return {ans} but returned {result}'

    # should throw ValueError
    # s.pop()