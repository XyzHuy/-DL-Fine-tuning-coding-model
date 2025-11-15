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
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Split the input string by commas to get the list of nodes
        nodes = preorder.split(',')
        
        # Initialize a stack to keep track of the number of available slots
        stack = [1]  # We start with one slot for the root node
        
        for node in nodes:
            if not stack:
                # If there are no available slots, the serialization is invalid
                return False
            
            # Use up one slot
            stack[-1] -= 1
            
            if stack[-1] == 0:
                # If the current node uses up the last slot of its parent, pop the stack
                stack.pop()
            
            if node != '#':
                # If the current node is not null, it creates two new slots
                stack.append(2)
        
        # In the end, there should be no available slots left
        return not stack

def isValidSerialization(preorder: str) -> bool:
    return Solution().isValidSerialization(preorder)