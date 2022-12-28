from collections import deque
from typing import List 

class BinaryTreeNode:

    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left = left 
        self.right = right 

def make_tree_example() -> BinaryTreeNode:
    tree = BinaryTreeNode(314,
        left=BinaryTreeNode(6,
            left=BinaryTreeNode(271,
                left=BinaryTreeNode(28),
                right=BinaryTreeNode(0)
                ),
            right=BinaryTreeNode(561,
                left=None,
                right=BinaryTreeNode(3,
                    left=BinaryTreeNode(17),
                    right=None
                )
            )
        ),
        right=BinaryTreeNode(7,
            left=BinaryTreeNode(2,
                left=None,
                right=BinaryTreeNode(1,
                    left=BinaryTreeNode(401,
                        left=None,
                        right=BinaryTreeNode(641)
                    ),
                    right=BinaryTreeNode(257)
                )
            ),
            right=BinaryTreeNode(272,
                left=None,
                right=BinaryTreeNode(29)
            )
        )
    )
    return tree


def traversal_preorder(root: BinaryTreeNode) -> None:
    ''' 
    vist root, visit left subtree, then visit right subtree
    '''
    if root:
        print(root.data, end=' ')
        traversal_preorder(root.left)
        traversal_preorder(root.right)


def traversal_inorder(root: BinaryTreeNode) -> None:
    ''' 
    visit left subtree, vist root, then visit right subtree
    '''
    if root:
        traversal_inorder(root.left)
        print(root.data, end=' ')
        traversal_inorder(root.right)


def traversal_postorder(root: BinaryTreeNode) -> None:
    ''' 
    visit left subtree, visit right subtree, then vist root
    '''
    if root:
        traversal_postorder(root.left)
        traversal_postorder(root.right)
        print(root.data, end=' ')


def traversal_postorder_list(root: BinaryTreeNode) -> List[int]:
    def postorder_helper(root: BinaryTreeNode) -> None:
        if root:
            postorder_helper(root.left)
            postorder_helper(root.right)
            result.append(root.data)

    result = []

    if not root:
        return result

    postorder_helper(root)

    return result
    


def traversal_levelorder(root: BinaryTreeNode) -> None:
    '''
    use a queue
    '''
    if root is None:
        return 

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        print(node.data, end=' ')

        # add children to queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)



def height(root: BinaryTreeNode) -> int:
    if root is None:
        return 0

    # depth first search/post order
    return 1 + max([height(root.left), height(root.right)])


def size(root: BinaryTreeNode) -> int:
    if root is None:
        return 0
    
    return 1 + size(root.left) + size(root.right)
    

def insert(root: BinaryTreeNode, data) -> None:
    node = BinaryTreeNode(data)

    if root is None:
        root = node
        return

    # level-order traversal
    q = deque()
    q.append(root)

    while q:
        temp = q.popleft()

        if temp.left:
            q.append(temp.left)
        else:
            temp.left = node 
            return

        if temp.right:
            q.append(temp.right)
        else:
            temp.right = node 
            return


if __name__ == '__main__':

    tree = make_tree_example()

    print('pre-order traveral:')
    traversal_preorder(tree)
    print('\nin-order traveral:')
    traversal_inorder(tree)
    print('\npost-order traveral:')
    traversal_postorder(tree)
    print('\nlevel-order traveral:')
    traversal_levelorder(tree)
    print('\nTree height:', height(tree))
    print('Tree size:', size(tree))
    insert(tree, 1000)
    print('Inserting node')
    print('level-order:')
    traversal_levelorder(tree)

    print('\n', traversal_postorder_list(tree))
