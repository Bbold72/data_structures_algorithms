from typing import List

# In a Min Binary Heap, the key at root must be minimum among all keys present in Binary Heap. 
# The same property must be recursively true for all nodes in Binary Tree.
# Time Complexity:
    # - Peek: O(1)
    # - extract/insert: O(log(n))
class MinHeap:


    def __init__(self, capacity: int=4):
        self._capacity: int = capacity
        self._array: List = [None] * self._capacity
        self._size: int = 0

    def is_empty(self) -> bool:
        return self._size == 0

    def _grow_heap(self) -> None:
        print('growing!')
        self._capacity *= 2
        temp = [None] * self._capacity
        temp[:self._size] = self._array[:self._size]
        self._array = temp


    def _swap(self, i: int, j: int) -> None:
        self._array[i], self._array[j] = self._array[j], self._array[i]


    def _heapify_up(self, child_index: int) -> None:
        parent_index = (child_index - 1) // 2

        # if heap propery is violated swap
        if parent_index >= 0 and self._array[parent_index] > self._array[child_index]:
            self._swap(parent_index, child_index)
            self._heapify_up(parent_index)

    def _min_child_index(self, left_child_index: int, right_child_index: int) -> None:
        if self._array[right_child_index] is None:   # right child empty
            return left_child_index
        else:
            return left_child_index if self._array[left_child_index] < self._array[right_child_index] else right_child_index

    def _heapify_down(self, parent_index: int=0) -> None:
        left_child_index = parent_index * 2 + 1
        right_child_index = left_child_index + 1
        if left_child_index > self._capacity or (self._array[left_child_index] is None and self._array[right_child_index] is None): # leaf 
            return
        else:
            min_child_index = self._min_child_index(left_child_index, right_child_index)
            if self._array[parent_index] > self._array[min_child_index]:
                # swap
                self._swap(parent_index, min_child_index)
                self._heapify_down(min_child_index)


    def insert(self, value) -> None:
        if self._size == self._capacity:
            self._grow_heap()

        # insert element at end of heap
        self._array[self._size] = value 

        if self._size > 0:
            self._heapify_up(self._size)
        self._size += 1


    def pop(self):
        if self.is_empty():
            raise IndexError('Heap is empty')

        value = self._array[0]

        # swap with last value
        self._size -= 1
        self._array[0], self._array[self._size] = self._array[self._size], None
        
        self._heapify_down()

        return value

    def __repr__(self) -> str:
        return str(self._array)

    def peek(self) -> int:
        return self._array[0]

    
if __name__ == '__main__':
    h = MinHeap()
    print(h)
    h.insert(1)
    h.insert(10)
    print(h)
    for i in range(10):
        print(i)
        h.insert(i)
    print(h)
    print(h.pop())
    print(h)
    print(h.pop())
    print(h)
    h.insert(20)
    h.insert(6)
    print(h)
    print(h.peek())
    print(h)