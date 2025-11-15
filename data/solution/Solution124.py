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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal max_sum
            if not node:
                return 0
            
            # Recursively get the maximum gain from the left and right subtrees
            left_gain = max(helper(node.left), 0)  # If the gain is negative, we treat it as 0
            right_gain = max(helper(node.right), 0)  # If the gain is negative, we treat it as 0
            
            # Calculate the price of the new path
            price_newpath = node.val + left_gain + right_gain
            
            # Update the maximum sum if the new path is better
            max_sum = max(max_sum, price_newpath)
            
            # For recursion, return the maximum gain the current node can contribute to its parent
            return node.val + max(left_gain, right_gain)
        
        max_sum = float('-inf')
        helper(root)
        return max_sum

def maxPathSum(root: Optional[TreeNode]) -> int:
    return Solution().maxPathSum(root)