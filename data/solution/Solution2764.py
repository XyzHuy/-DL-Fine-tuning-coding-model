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
from typing import List

class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        # Stack to keep track of the expected parent nodes
        stack = []
        
        for node_id, parent_id in nodes:
            # While the stack is not empty and the top of the stack is not the parent of the current node
            while stack and stack[-1] != parent_id:
                stack.pop()
            
            # If the stack is empty and the current node is not the root (parent_id != -1), it's invalid
            if not stack and parent_id != -1:
                return False
            
            # Push the current node to the stack
            stack.append(node_id)
        
        return True

def isPreorder(nodes: List[List[int]]) -> bool:
    return Solution().isPreorder(nodes)