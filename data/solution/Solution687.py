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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            # Recursively find the longest univalue path in the left and right subtrees
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            
            # Initialize the lengths of the left and right arms
            left_arm = right_arm = 0
            
            # Check if the left child exists and has the same value as the current node
            if node.left and node.left.val == node.val:
                left_arm = left_length + 1
            
            # Check if the right child exists and has the same value as the current node
            if node.right and node.right.val == node.val:
                right_arm = right_length + 1
            
            # Update the result with the maximum path found so far
            self.result = max(self.result, left_arm + right_arm)
            
            # Return the longer arm to the parent node
            return max(left_arm, right_arm)
        
        self.result = 0
        dfs(root)
        return self.result

def longestUnivaluePath(root: Optional[TreeNode]) -> int:
    return Solution().longestUnivaluePath(root)