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
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        lonely_nodes = []
        
        def dfs(node):
            if not node:
                return
            
            # Check if the current node has only one child
            if node.left and not node.right:
                lonely_nodes.append(node.left.val)
            elif node.right and not node.left:
                lonely_nodes.append(node.right.val)
            
            # Recur for left and right children
            dfs(node.left)
            dfs(node.right)
        
        # Start DFS from the root
        dfs(root)
        
        return lonely_nodes

def getLonelyNodes(root: Optional[TreeNode]) -> List[int]:
    return Solution().getLonelyNodes(root)