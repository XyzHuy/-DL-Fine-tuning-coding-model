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
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0, 0  # sum, count, match_count
            
            # Recursively get the sum, count, and match_count for left and right subtrees
            left_sum, left_count, left_match = dfs(node.left)
            right_sum, right_count, right_match = dfs(node.right)
            
            # Calculate the sum, count, and average for the current subtree
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            current_average = current_sum // current_count
            
            # Check if the current node's value matches the average of its subtree
            current_match = left_match + right_match + (current_average == node.val)
            
            return current_sum, current_count, current_match
        
        # Start the DFS from the root and return the match_count for the entire tree
        _, _, match_count = dfs(root)
        return match_count

def averageOfSubtree(root: TreeNode) -> int:
    return Solution().averageOfSubtree(root)