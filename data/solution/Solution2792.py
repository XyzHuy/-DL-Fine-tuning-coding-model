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
    def countGreatEnoughNodes(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if not node:
                return [], 0
            
            # Recursively get the smallest k values from the left and right subtrees
            left_values, left_count = dfs(node.left)
            right_values, right_count = dfs(node.right)
            
            # Merge the values from left and right subtrees and add the current node's value
            all_values = left_values + right_values + [node.val]
            all_values.sort()
            
            # Keep only the smallest k values
            if len(all_values) > k:
                all_values = all_values[:k]
            
            # Check if the current node is great enough
            count = left_count + right_count
            if len(all_values) >= k and all_values[k-1] < node.val:
                count += 1
            
            return all_values, count
        
        _, result = dfs(root)
        return result

def countGreatEnoughNodes(root: Optional[TreeNode], k: int) -> int:
    return Solution().countGreatEnoughNodes(root, k)