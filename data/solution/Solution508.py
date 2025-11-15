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
from collections import defaultdict
from typing import List, Optional

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def subtreeSum(node):
            if not node:
                return 0
            left_sum = subtreeSum(node.left)
            right_sum = subtreeSum(node.right)
            current_sum = node.val + left_sum + right_sum
            sum_count[current_sum] += 1
            return current_sum
        
        sum_count = defaultdict(int)
        subtreeSum(root)
        
        max_freq = max(sum_count.values())
        return [s for s in sum_count if sum_count[s] == max_freq]

def findFrequentTreeSum(root: Optional[TreeNode]) -> List[int]:
    return Solution().findFrequentTreeSum(root)