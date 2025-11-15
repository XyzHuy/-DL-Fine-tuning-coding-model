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
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node, parent_val, current_length):
            if not node:
                return current_length
            
            # Check if the current node is consecutive
            if node.val == parent_val + 1:
                current_length += 1
            else:
                current_length = 1
            
            # Recur for left and right children and return the maximum length found
            left_length = dfs(node.left, node.val, current_length)
            right_length = dfs(node.right, node.val, current_length)
            
            return max(current_length, left_length, right_length)
        
        # Start DFS from the root with initial parent value as -inf and length 0
        return dfs(root, float('-inf'), 0)

def longestConsecutive(root: Optional[TreeNode]) -> int:
    return Solution().longestConsecutive(root)