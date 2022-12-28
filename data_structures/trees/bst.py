from data_structures.trees import binary
from data_structures.trees.binary import BinaryTreeNode

def make_tree_example() -> BinaryTreeNode:
    root = BinaryTreeNode(19,
        left=BinaryTreeNode(7,
            left=BinaryTreeNode(3,
                left=BinaryTreeNode(2),
                right=BinaryTreeNode(5)
                ),
            right=BinaryTreeNode(11,
                right=BinaryTreeNode(17,
                    left=BinaryTreeNode(13)
                    )
                )
            ),
        right=BinaryTreeNode(43,
            left=BinaryTreeNode(23,
                right=BinaryTreeNode(37,
                    left=BinaryTreeNode(29,
                        right=BinaryTreeNode(31)
                        ),
                    right=BinaryTreeNode(41)
                    )
                ),
            right=BinaryTreeNode(47,
                right=BinaryTreeNode(53)
            )
        )
    )
    return root


def insert(root: BinaryTreeNode, data: int) -> BinaryTreeNode:
    ''' 
    assumes tree holds unique set of values
    '''
    if root is None:
        return BinaryTreeNode(data)
    else:
        if root.data == data:
            return root
        elif root.data < data:
            root.right = insert(root.right, data)
        else:
            root.left = insert(root.left, data)
    return root
    

def search_path(root: BinaryTreeNode, key: int) -> None:
    ''' 
    prints path to node 
    '''
    if root:
        print(root.data, end=' ')
    else:
        print('Not found', end=' ')
        return

    if root.data == key:
        return
    elif root.data < key:
        search_path(root.right, key)
    else:
        search_path(root.left, key)


def get_min(root: BinaryTreeNode) -> BinaryTreeNode: 
    current = root
 
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
 
    return current


def get_max(root: BinaryTreeNode) -> BinaryTreeNode: 
    current = root
 
    # loop down to find the leftmost leaf
    while(current.right is not None):
        current = current.right
 
    return current
        

def delete(root: BinaryTreeNode, key: int) -> BinaryTreeNode:
    if root is None:
        return root 

    if root.data < key:
        root.right = delete(root.right, key)

    elif root.data > key:
        root.left = delete(root.left, key)

    # If key is same as root's key, 
    # then this is the node to be deleted
    else:
 
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 
        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = get_min(root.right)
 
        # Copy the inorder successor's
        # content to this node
        root.data = temp.data
 
        # Delete the inorder successor
        root.right = delete(root.right, temp.data)
 
    return root


if __name__ == '__main__':

    bst = make_tree_example()
    binary.traversal_levelorder(bst)

    print('\n\nInsertion:')
    print('Insert 18')
    print('Insert 45')
    bst = insert(bst, 18)
    bst = insert(bst, 45)
    binary.traversal_levelorder(bst)

    print('\n\nSearching:')
    bst = make_tree_example()
    print('Find 31')
    search_path(bst, 31)
    print('\nFind 32')
    search_path(bst, 32)
    print('\nFind 11')
    search_path(bst, 11)

    print('\n\nMinimum:')
    print(get_min(bst))

    print('\nMaximum:')
    print(get_max(bst))

    print('\nDeletion:')
    print('Delete 31')
    bst = delete(bst, 31)
    binary.traversal_levelorder(bst)

    bst = make_tree_example()
    print('\nDelete 47')
    bst = delete(bst, 47)
    binary.traversal_levelorder(bst)

    print('\nDelete 19')
    bst = make_tree_example()
    bst = delete(bst, 19)
    binary.traversal_levelorder(bst)
