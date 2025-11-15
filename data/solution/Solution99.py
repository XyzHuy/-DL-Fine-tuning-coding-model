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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Initialize pointers to track the two swapped nodes
        first = second = prev = None
        
        # Morris Traversal for in-order traversal
        current = root
        while current:
            if current.left is None:
                # Check if the current node is out of order
                if prev and prev.val > current.val:
                    if not first:
                        first = prev
                    second = current
                prev = current
                current = current.right
            else:
                # Find the predecessor of the current node
                pre = current.left
                while pre.right and pre.right != current:
                    pre = pre.right
                
                if pre.right is None:
                    # Establish a temporary link to the current node
                    pre.right = current
                    current = current.left
                else:
                    # Remove the temporary link
                    pre.right = None
                    # Check if the current node is out of order
                    if prev and prev.val > current.val:
                        if not first:
                            first = prev
                        second = current
                    prev = current
                    current = current.right
        
        # Swap the values of the two nodes
        if first and second:
            first.val, second.val = second.val, first.val

def recoverTree(root: Optional[TreeNode]) -> None:
    return Solution().recoverTree(root)