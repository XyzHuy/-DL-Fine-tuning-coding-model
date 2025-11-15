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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_number):
            if not node:
                return 0
            
            # Shift the current number left by 1 (equivalent to multiplying by 2) and add the node's value
            current_number = (current_number << 1) | node.val
            
            # If it's a leaf node, return the current number
            if not node.left and not node.right:
                return current_number
            
            # Otherwise, sum the results of the left and right subtrees
            return dfs(node.left, current_number) + dfs(node.right, current_number)
        
        return dfs(root, 0)

def sumRootToLeaf(root: Optional[TreeNode]) -> int:
    return Solution().sumRootToLeaf(root)