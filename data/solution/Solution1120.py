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
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.max_average = 0.0
        
        def dfs(node):
            if not node:
                return 0, 0  # (sum, count)
            
            # Recursively get sum and count of nodes in left and right subtrees
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            # Calculate sum and count including the current node
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            
            # Calculate the average of the current subtree
            current_average = total_sum / total_count
            
            # Update the maximum average found so far
            self.max_average = max(self.max_average, current_average)
            
            return total_sum, total_count
        
        dfs(root)
        return self.max_average

def maximumAverageSubtree(root: Optional[TreeNode]) -> float:
    return Solution().maximumAverageSubtree(root)