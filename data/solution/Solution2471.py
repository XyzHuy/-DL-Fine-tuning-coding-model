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
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        
        def min_swaps_to_sort(arr):
            n = len(arr)
            arrpos = [*enumerate(arr)]
            arrpos.sort(key=lambda x: x[1])
            visited = {k: False for k in range(n)}
            swaps = 0
            
            for i in range(n):
                if visited[i] or arrpos[i][0] == i:
                    continue
                
                cycle_size = 0
                j = i
                
                while not visited[j]:
                    visited[j] = True
                    j = arrpos[j][0]
                    cycle_size += 1
                
                if cycle_size > 0:
                    swaps += (cycle_size - 1)
            
            return swaps
        
        if not root:
            return 0
        
        queue = deque([root])
        operations = 0
        
        while queue:
            level_size = len(queue)
            level_nodes = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            operations += min_swaps_to_sort(level_nodes)
        
        return operations

def minimumOperations(root: Optional[TreeNode]) -> int:
    return Solution().minimumOperations(root)