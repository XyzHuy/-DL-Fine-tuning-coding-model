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
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        def inorder_traversal(node, values):
            if node:
                inorder_traversal(node.left, values)
                values.append(node.val)
                inorder_traversal(node.right, values)
        
        # Get sorted list of values from both BSTs
        values1 = []
        values2 = []
        inorder_traversal(root1, values1)
        inorder_traversal(root2, values2)
        
        # Use two pointers to find if there exist two numbers that sum to target
        i, j = 0, len(values2) - 1
        while i < len(values1) and j >= 0:
            current_sum = values1[i] + values2[j]
            if current_sum == target:
                return True
            elif current_sum < target:
                i += 1
            else:
                j -= 1
        
        return False

def twoSumBSTs(root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
    return Solution().twoSumBSTs(root1, root2, target)