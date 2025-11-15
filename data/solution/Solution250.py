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
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        
        def is_unival(node):
            if not node:
                return True, None
            
            left_is_unival, left_val = is_unival(node.left)
            right_is_unival, right_val = is_unival(node.right)
            
            if left_is_unival and right_is_unival:
                if (left_val is None or left_val == node.val) and (right_val is None or right_val == node.val):
                    self.count += 1
                    return True, node.val
            
            return False, node.val
        
        is_unival(root)
        return self.count

def countUnivalSubtrees(root: Optional[TreeNode]) -> int:
    return Solution().countUnivalSubtrees(root)