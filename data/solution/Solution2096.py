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
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findLCA(node, startValue, destValue):
            if not node:
                return None
            if node.val == startValue or node.val == destValue:
                return node
            left = findLCA(node.left, startValue, destValue)
            right = findLCA(node.right, startValue, destValue)
            if left and right:
                return node
            return left if left else right
        
        def findPath(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            if node.left and findPath(node.left, target, path):
                path.append('L')
            elif node.right and findPath(node.right, target, path):
                path.append('R')
            return len(path) > 0
        
        lca = findLCA(root, startValue, destValue)
        
        start_path = []
        dest_path = []
        
        findPath(lca, startValue, start_path)
        findPath(lca, destValue, dest_path)
        
        # The path from start to LCA is all 'U' moves
        start_to_lca = 'U' * len(start_path)
        # The path from LCA to dest is the reverse of dest_path
        lca_to_dest = ''.join(reversed(dest_path))
        
        return start_to_lca + lca_to_dest

def getDirections(root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    return Solution().getDirections(root, startValue, destValue)