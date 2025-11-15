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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Initialize a queue with tuples of (node, index)
        queue = [(root, 0)]
        max_width = 0
        
        while queue:
            level_length = len(queue)
            _, first_index = queue[0]  # First index of the current level
            _, last_index = queue[-1]  # Last index of the current level
            
            # Calculate the width of the current level
            max_width = max(max_width, last_index - first_index + 1)
            
            # Process all nodes at the current level
            for _ in range(level_length):
                node, index = queue.pop(0)
                
                # If there is a left child, add it to the queue with the correct index
                if node.left:
                    queue.append((node.left, 2 * index))
                
                # If there is a right child, add it to the queue with the correct index
                if node.right:
                    queue.append((node.right, 2 * index + 1))
        
        return max_width

def widthOfBinaryTree(root: Optional[TreeNode]) -> int:
    return Solution().widthOfBinaryTree(root)