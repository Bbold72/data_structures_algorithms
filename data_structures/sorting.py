import random
from typing import List

def selection_sort(A: List[int]) -> None:
    ''' 
    The selection sort algorithm sorts an array by repeatedly 
    finding the minimum element (considering ascending order) 
    from the unsorted part and putting it at the beginning. 

    Algorithm:
        - Initialize minimum value(min_idx) to location 0.
        - Traverse the array to find the minimum element in the array.
        - While traversing if any element smaller than min_idx is found then swap both the values.
        - Then, increment min_idx to point to the next element.
        - Repeat until the array is sorted.
    O(n^2) time and O(1) space complexity
    '''
    for i in range(len(A)):

        # find next smallest value
        min_index = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        
        # switch i,j
        A[i], A[min_index] = A[min_index], A[i]


def insertion_sort(A: List[int]) -> None:
    '''
    Insertion sort is a simple sorting algorithm that works similar to the 
    way you sort playing cards in your hands. The array is virtually split 
    into a sorted and an unsorted part. Values from the unsorted part 
    are picked and placed at the correct position in the sorted part.

    Characteristics of Insertion Sort:
        - This algorithm is one of the simplest algorithm with simple implementation
        - Basically, Insertion sort is efficient for small data values
        - Insertion sort is adaptive in nature, i.e. it is appropriate for data sets which are already partially sorted.

    Algorithm:
        - To sort an array of size N in ascending order: 
        - Iterate from arr[1] to arr[N] over the array. 
        - Compare the current element (key) to its predecessor. 
        - If the key element is smaller than its predecessor, compare it to the elements before. 
            Move the greater elements one position up to make space for the swapped element.

    O(n^2) time and O(1) space complexity
    '''
    for i in range(1, len(A)):

        key = A[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j] 
            j -= 1
        
        A[j+1] = key


def merge_sort(A: List[int]) -> None:
    ''' 
    The Merge Sort algorithm is a sorting algorithm that is based on the Divide and Conquer paradigm. 
    In this algorithm, the array is initially divided into two equal halves and then they are combined in a sorted manner.
    Think of it as a recursive algorithm that continuously splits the array in half until it cannot be further divided. 
    This means that if the array becomes empty or has only one element left, the dividing will stop, 
    i.e. it is the base case to stop the recursion. If the array has multiple elements, 
    split the array into halves and recursively invoke the merge sort on each of the halves. 
    Finally, when both halves are sorted, the merge operation is applied. Merge operation is the process 
    of taking two smaller sorted arrays and combining them to eventually make a larger one.

    O(nlog(n)) time and O(n) space complexity and a stable sort
    '''
    if len(A) > 1:   # so dont infinitely recurse
        # split into two halves
        mid = len(A) // 2 
        left, right = A[:mid], A[mid:]
        
        # sort each half
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1


def merge_sort2(A: List[int], bottom_up: bool=False) -> None:

    def merge(lo: int, mid: int, hi: int) -> None:
        i, j = lo, mid + 1

        # copy A into aux
        aux = A.copy() 

        k = lo 
        while k <= hi:
            if i > mid:           # exhausted first half of array
                A[k] = aux[j]
                j += 1
            elif j > hi:          # exhausted second half of array
                A[k] = aux[i]
                i += 1
            elif aux[i] < aux[j]:
                A[k] = aux[i]
                i += 1
            else:
                A[k] = aux[j]
                j += 1
            k += 1

    def sort(lo: int, hi: int) -> None:
        if hi <= lo:
            return

        mid = lo + (hi - lo) // 2
        sort(lo, mid)
        sort(mid+1, hi)
        merge(lo, mid, hi)

    def sort_bottom_up() -> None:
        N = len(A)

        sz = 1
        while sz < N:
            lo = 0
            while lo < N - sz:
                merge(lo, lo+sz-1, min([lo + sz + sz-1, N-1]))
                lo += sz+sz
            sz = sz+sz

    if bottom_up:
        sort_bottom_up() 
    else: 
        sort(0, len(A)-1)


def partition(A: List[int], lo: int, hi: int) -> None:
    i = lo + 1
    j = hi 
    pivot_value = A[lo]

    while True:
        # find left item to swap
        while A[i] < pivot_value:
            i += 1
            if i > hi:
                break
        
        # find right item to swap
        while A[j] > pivot_value:
            j -= 1
            if j == lo:
                break
        
        # check if pointers cross 
        if i >= j:
            break 

        # swap i and j
        A[i], A[j] = A[j], A[i]

    # swap partitioning item
    A[lo], A[j] = A[j], A[lo]

    # correct place in array for partition
    return j
    


def quick_sort(A: List[int]) -> None:

    def sort(lo: int, hi: int) -> None:
        if lo >= hi:
            return
        k = partition(A, lo, hi)
        sort(lo, k-1)
        sort(k+1, hi)

    random.shuffle(A)
    sort(0, len(A)-1)


def quick_select(A: List[int], k: int) -> int:
    ''' 
    return kth largest
    '''
    random.shuffle(A)
    lo, hi = 0, len(A) - 1
    # 1st smallest is 0 index, 2nd smallest is 1 index, ...
    k -= 1   

    while lo < hi:
        i = partition(A, lo, hi)
        if i > k:
            hi = i - 1
        elif i < k:
            lo = i + 1
        else:
            return A[i]

    return A[lo]


def quick_sort_3way(A: List[int]) -> None: 

    def partition3way(lo: int, hi: int) -> None:
        if lo >= hi:
            return
        lt, gt = lo, hi 
        pivot_value = A[lo]
        i = lo + 1

        while i <= gt:
            if A[i] < pivot_value:
                A[i], A[lt] = A[lt], A[i]
                i += 1
                lt += 1
            elif A[i] > pivot_value:
                A[i], A[gt] = A[gt], A[i]
                gt -= 1
            # i equal to pivot
            else:
                i += 1
        
        partition3way(lo, lt-1)
        partition3way(gt+1, hi)

    random.shuffle(A)
    partition3way(0, len(A) - 1)


def heap_sort(A: List[int]) -> None:
    def heapify(A: List[int], N: int, i: int) -> None:
        largest = A[i]
        left = 2*i + 1
        right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if left < N and A[largest] < A[left]:
            largest = left
 
        # See if right child of root exists and is
        # greater than root
        if right < N and A[largest] < A[right]:
            largest = right
 
        # Change root, if needed
        if largest != i:
            A[i], A[largest] = A[largest], A[i]  # swap
    
            # Heapify the root.
            heapify(A, N, largest)

    N = len(A)
 
    # Build a maxheap.
    for i in range(N//2 - 1, -1, -1):
        heapify(A, N, i)
 
    # One by one extract elements
    for i in range(N-1, 0, -1):
        A[i], A[0] = A[0], A[i]  # swap
        heapify(A, i, 0)

def make_example() -> List[int]:
    return [4, 1, 10, 3, 2, 4, 1, 5, 9, 8, 4, 15]



if __name__ == '__main__':
    A = make_example() 
    print(A)
    print() 

    print('Selection Sort:')
    selection_sort(A)
    print(A)

    print('\nInsertion Sort:')
    A = make_example() 
    insertion_sort(A)
    print(A)

    
    print('\nMerge Sort:')
    A = make_example() 
    merge_sort(A)
    print(A)


    print('\nMerge Sort V2:')
    A = make_example() 
    merge_sort2(A)
    print(A)


    print('\nBottom Up Merge Sort:')
    A = make_example() 
    merge_sort2(A, bottom_up=True)
    print(A)


    print('\nQuick Sort:')
    A = [4, 1, 10, 3, 2, 11, 0, 5, 9, 8, 6, 15]
    quick_sort(A)
    print(A)


    print('\nQuick Select:')
    A = [4, 1, 10, 3, 2, 11, 0, 5, 9, 8, 6, 15]
    print('1st Smallest: ', quick_select(A, 1))
    print('8th Smallest: ', quick_select(A, 8))
    print('12th Smallest: ', quick_select(A, 12))


    print('\n3-Way Quick Sort :')
    A = make_example() 
    quick_sort_3way(A)
    print(A)


    print('\nHeap Sort:')
    A = make_example() 
    heap_sort(A)
    print(A)