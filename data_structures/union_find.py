from typing import Dict, List

class UnionFind:

    def __init__(self, n: int) -> None:
 
        self._count: int = n          # number of connected components
        self._size: List[int] = [1] * n
        self._id: List[int] = [i for i in range(n)]
        self._n: int = n

    
    def count(self) -> int:
        ''' 
        return number of connected components
        '''
        return self._count

    
    def _root(self, i: int) -> int:
        ''' 
        return root of i
        '''
        root = i

        # find root
        while root != self._id[root]:
            root = self._id[root]
        
        # path compression:
        # assign all visited ids to root
        while i != self._id[i]:
            self._id[i], i = root, self._id[i]

        return root


    # def _root(self, i: int) -> int:
    #     ''' 
    #     return root of i
    #     with recursion and path compression
    #     '''
    #     if i != self._id[i]:
    #         self._id[i] = self._root(self._id[i])
    #     return self._id[i]


    def connected(self, p: int, q: int) -> bool:
        '''  
        check _root()if two values are connected
        '''
        return self._root(p) == self._root(q)


    def union(self, p: int, q: int) -> None:
        ''' 
        merge two components by updating root ids
        keep tree shallow by adding smaller tree to larger tree
        '''
        i = self._root(p)
        j = self._root(q)

        # if not already connected, union
        if i != j:
            # add nodes of smaller tree to bigger tree
            if self._size[i] < self._size[j]:
                self._id[i] = j
                self._size[j] += self._size[i] 
            else:
                self._id[j] = i
                self._size[i] += self._size[j]  

            self._count -= 1   # one less component sinced union'd


    def get_set(self, p: int) -> List[int]: 
        '''
        given a point p, return all points it is connected to 
        '''
        root = self._root(p) 
        return [i for i in range(self._n) if root == self._root(self._id[i])]


    def get_all_sets(self) -> List[List[int]]:
        root_idx_map: Dict[int, int] = {}
        curr_set_id: int = 0
        result: List[List[int]] = []

        for i, id in enumerate(self._id):
            root = self._root(i)
            try:
                set_id = root_idx_map[root]
                result[set_id].append(i)
            except KeyError:
                root_idx_map[root] = curr_set_id
                set_id = curr_set_id
                curr_set_id += 1
                result.append([i])
        return result

if '__main__' == __name__:

    uf = UnionFind(10)
    uf.union(0, 9)
    uf.union(1, 5)
    uf.union(4, 8)
    uf.union(4, 3)
    uf.union(0, 8)
    uf.union(6, 7)

    assert uf.count() == 4
    assert uf.connected(0, 9) is True
    assert uf.connected(3, 8) is True
    assert uf.connected(1, 5) is True
    assert uf.connected(6, 7) is True
    assert uf.connected(5, 6) is False
    assert uf.connected(9, 2) is False
    assert uf.connected(4, 5) is False
    print(uf._id)
    print(uf.get_set(0))
    print(uf.get_all_sets())
