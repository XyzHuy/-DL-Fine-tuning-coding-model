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
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # Initialize the second minimum to infinity
        self.second_min = float('inf')
        # The smallest value in the tree is the root's value
        self.min_value = root.val
        
        def dfs(node):
            if not node:
                return
            
            # If we found a value that is different from the smallest value
            # and it is smaller than the current second minimum, update it
            if self.min_value < node.val < self.second_min:
                self.second_min = node.val
            
            # Recur for left and right subtrees
            dfs(node.left)
            dfs(node.right)
        
        # Start DFS from the root
        dfs(root)
        
        # If second_min is still infinity, it means there was no second minimum value
        return self.second_min if self.second_min != float('inf') else -1

def findSecondMinimumValue(root: Optional[TreeNode]) -> int:
    return Solution().findSecondMinimumValue(root)