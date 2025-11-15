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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, max_anc, min_anc):
            if not node:
                return max_anc - min_anc
            
            max_anc = max(max_anc, node.val)
            min_anc = min(min_anc, node.val)
            
            left_diff = dfs(node.left, max_anc, min_anc)
            right_diff = dfs(node.right, max_anc, min_anc)
            
            return max(left_diff, right_diff)
        
        return dfs(root, root.val, root.val)

def maxAncestorDiff(root: Optional[TreeNode]) -> int:
    return Solution().maxAncestorDiff(root)