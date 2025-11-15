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
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.count = 0
        
        def dfs(node):
            if not node:
                return []
            
            # If the node is a leaf, return a list with a single element 1, representing a leaf node at distance 1
            if not node.left and not node.right:
                return [1]
            
            # Recursively get the distances of leaf nodes in the left and right subtrees
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Count pairs of leaf nodes from left and right subtrees that are within the given distance
            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        self.count += 1
            
            # Return the distances of leaf nodes from the current node, incrementing each by 1
            return [d + 1 for d in left_distances + right_distances]
        
        dfs(root)
        return self.count

def countPairs(root: Optional[TreeNode], distance: int) -> int:
    return Solution().countPairs(root, distance)