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
from typing import List

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # Create a dictionary to store the tree nodes
        tree = {}
        
        # Populate the tree dictionary
        for num in nums:
            depth = num // 100
            position = (num // 10) % 10
            value = num % 10
            tree[(depth, position)] = value
        
        # Initialize the total sum of paths
        total_sum = 0
        
        # Stack to perform DFS, storing (depth, position, path_sum)
        stack = [(1, 1, 0)]
        
        while stack:
            current_depth, current_position, path_sum = stack.pop()
            current_value = tree[(current_depth, current_position)]
            path_sum += current_value
            
            # Calculate the positions of the left and right children
            left_child = (current_depth + 1, current_position * 2 - 1)
            right_child = (current_depth + 1, current_position * 2)
            
            # Check if the node is a leaf
            if left_child not in tree and right_child not in tree:
                total_sum += path_sum
            else:
                # Add children to the stack if they exist
                if left_child in tree:
                    stack.append((left_child[0], left_child[1], path_sum))
                if right_child in tree:
                    stack.append((right_child[0], right_child[1], path_sum))
        
        return total_sum

def pathSum(nums: List[int]) -> int:
    return Solution().pathSum(nums)