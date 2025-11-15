import heapq
import itertools
from sortedcontainers import SortedList
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, remaining_sum, path, result):
            if not node:
                return
            
            # Add the current node to the path
            path.append(node.val)
            
            # Check if it's a leaf node and the path sum equals the target sum
            if not node.left and not node.right and remaining_sum == node.val:
                result.append(list(path))
            
            # Recurse on the left and right children
            dfs(node.left, remaining_sum - node.val, path, result)
            dfs(node.right, remaining_sum - node.val, path, result)
            
            # Backtrack: remove the current node from the path
            path.pop()
        
        result = []
        dfs(root, targetSum, [], result)
        return result

def pathSum(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    return Solution().pathSum(root, targetSum)