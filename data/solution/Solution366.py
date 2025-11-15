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
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def collectLeaves(node):
            if not node:
                return -1
            
            # Recursively collect leaves from the left and right subtrees
            left_height = collectLeaves(node.left)
            right_height = collectLeaves(node.right)
            
            # Current node's height is the max of its subtrees' heights plus one
            current_height = max(left_height, right_height) + 1
            
            # Ensure the result list has a list for the current height
            if current_height >= len(result):
                result.append([])
            
            # Add the current node's value to the list corresponding to its height
            result[current_height].append(node.val)
            
            return current_height
        
        result = []
        collectLeaves(root)
        return result

def findLeaves(root: Optional[TreeNode]) -> List[List[int]]:
    return Solution().findLeaves(root)