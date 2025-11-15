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
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        # Find the maximum value and its index in the current list
        max_val = max(nums)
        max_index = nums.index(max_val)
        
        # Create the root node with the maximum value
        root = TreeNode(max_val)
        
        # Recursively build the left subtree with elements before the maximum value
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        
        # Recursively build the right subtree with elements after the maximum value
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        
        return root

def constructMaximumBinaryTree(nums: List[int]) -> Optional[TreeNode]:
    return Solution().constructMaximumBinaryTree(nums)