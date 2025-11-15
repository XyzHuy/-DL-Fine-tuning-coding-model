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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Step 1: Calculate the sum of values at each depth
        depth_sum = {}
        
        def calculate_depth_sum(node, depth):
            if not node:
                return
            if depth not in depth_sum:
                depth_sum[depth] = 0
            depth_sum[depth] += node.val
            calculate_depth_sum(node.left, depth + 1)
            calculate_depth_sum(node.right, depth + 1)
        
        calculate_depth_sum(root, 0)
        
        # Step 2: Replace each node's value with the sum of its cousins' values
        def replace_values(node, depth, sibling_sum):
            if not node:
                return
            node.val = depth_sum[depth] - sibling_sum
            left_val = (node.left.val if node.left else 0)
            right_val = (node.right.val if node.right else 0)
            replace_values(node.left, depth + 1, left_val + right_val)
            replace_values(node.right, depth + 1, left_val + right_val)
        
        replace_values(root, 0, root.val)
        return root

def replaceValueInTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    return Solution().replaceValueInTree(root)