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
from typing import List, Optional

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        parents = set()
        children = set()
        
        for parent_val, child_val, is_left in descriptions:
            # Create or get the parent node
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            parent_node = nodes[parent_val]
            
            # Create or get the child node
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
            child_node = nodes[child_val]
            
            # Assign the child to the parent
            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            
            # Track parents and children
            parents.add(parent_val)
            children.add(child_val)
        
        # The root is the node that is a parent but not a child
        root_val = (parents - children).pop()
        return nodes[root_val]

def createBinaryTree(descriptions: List[List[int]]) -> Optional[TreeNode]:
    return Solution().createBinaryTree(descriptions)