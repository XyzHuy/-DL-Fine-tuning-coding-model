import random
import functools
import collections
import string
import math
import datetime


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values: list):
    if not values:
        return None
    root = TreeNode(values[0])
    i = 1
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def is_same_tree(p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Helper function to perform in-order traversal and rearrange nodes
        def inorder(node):
            if not node:
                return
            
            # Traverse the left subtree
            inorder(node.left)
            
            # Rearrange nodes
            node.left = None
            self.current.right = node
            self.current = node
            
            # Traverse the right subtree
            inorder(node.right)
        
        # Create a dummy node to act as the new root
        dummy = TreeNode()
        self.current = dummy
        
        # Perform in-order traversal starting from the original root
        inorder(root)
        
        # Return the right child of dummy, which is the new root
        return dummy.right

def increasingBST(root: Optional[TreeNode]) -> Optional[TreeNode]:
    return Solution().increasingBST(root)