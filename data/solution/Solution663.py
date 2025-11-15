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
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        def get_total_sum(node):
            if not node:
                return 0
            return node.val + get_total_sum(node.left) + get_total_sum(node.right)
        
        def can_partition(node, total_sum):
            if not node:
                return 0, False
            
            left_sum, left_possible = can_partition(node.left, total_sum)
            if left_possible:
                return left_sum, True
            
            right_sum, right_possible = can_partition(node.right, total_sum)
            if right_possible:
                return right_sum, True
            
            current_sum = node.val + left_sum + right_sum
            if current_sum == total_sum // 2 and current_sum * 2 == total_sum:
                return current_sum, True
            
            return current_sum, False
        
        total_sum = get_total_sum(root)
        if total_sum % 2 != 0:
            return False
        
        _, result = can_partition(root.left, total_sum)
        if result:
            return True
        
        _, result = can_partition(root.right, total_sum)
        if result:
            return True
        
        return False

def checkEqualTree(root: Optional[TreeNode]) -> bool:
    return Solution().checkEqualTree(root)