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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        # Initialize the sum
        total_sum = 0
        
        # If the current node's value is within the range, add it to the sum
        if low <= root.val <= high:
            total_sum += root.val
        
        # If the current node's value is greater than low, there might be valid nodes in the left subtree
        if root.val > low:
            total_sum += self.rangeSumBST(root.left, low, high)
        
        # If the current node's value is less than high, there might be valid nodes in the right subtree
        if root.val < high:
            total_sum += self.rangeSumBST(root.right, low, high)
        
        return total_sum

def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    return Solution().rangeSumBST(root, low, high)