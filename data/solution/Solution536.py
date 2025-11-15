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
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        
        # Find the index of the first parenthesis
        idx = 0
        while idx < len(s) and (s[idx].isdigit() or s[idx] == '-'):
            idx += 1
        
        # The root value is from the start to the index found
        root = TreeNode(int(s[:idx]))
        
        # If there are no parenthesis, return the root node
        if idx == len(s):
            return root
        
        # Find the indices for the left and right subtrees
        open_count = 0
        start = idx
        for j in range(idx, len(s)):
            if s[j] == '(':
                open_count += 1
            elif s[j] == ')':
                open_count -= 1
            
            # When open_count is 0, we found a complete subtree
            if open_count == 0:
                if start == idx:
                    root.left = self.str2tree(s[start+1:j])
                    start = j + 1
                else:
                    root.right = self.str2tree(s[start+1:j])
        
        return root

def str2tree(s: str) -> Optional[TreeNode]:
    return Solution().str2tree(s)