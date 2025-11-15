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
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        flipped = []
        index = [0]
        
        def dfs(node):
            if not node:
                return True
            if node.val != voyage[index[0]]:
                return False
            index[0] += 1
            
            if (node.left and node.right and
                node.right.val == voyage[index[0]] and
                node.left.val != voyage[index[0]]):
                flipped.append(node.val)
                node.left, node.right = node.right, node.left
            
            return dfs(node.left) and dfs(node.right)
        
        return flipped if dfs(root) else [-1]

def flipMatchVoyage(root: Optional[TreeNode], voyage: List[int]) -> List[int]:
    return Solution().flipMatchVoyage(root, voyage)