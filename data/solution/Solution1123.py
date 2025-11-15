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
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return node, 0  # Return None and depth 0 for null nodes
            
            left_lca, left_depth = dfs(node.left)
            right_lca, right_depth = dfs(node.right)
            
            if left_depth == right_depth:
                return node, left_depth + 1  # Current node is the LCA of deepest leaves
            elif left_depth > right_depth:
                return left_lca, left_depth + 1  # LCA is in the left subtree
            else:
                return right_lca, right_depth + 1  # LCA is in the right subtree
        
        return dfs(root)[0]

def lcaDeepestLeaves(root: Optional[TreeNode]) -> Optional[TreeNode]:
    return Solution().lcaDeepestLeaves(root)