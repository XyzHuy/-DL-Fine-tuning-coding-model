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
from typing import Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Dictionary to store prefix sums and their frequencies
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # Base case: a prefix sum of 0 has one count
        
        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            if not node:
                return 0
            
            # Update the current sum
            current_sum += node.val
            
            # Calculate the number of paths that end at the current node
            paths_ending_here = prefix_sum_count[current_sum - targetSum]
            
            # Update the prefix sum count
            prefix_sum_count[current_sum] += 1
            
            # Recurse on the left and right subtrees
            paths_from_left = dfs(node.left, current_sum)
            paths_from_right = dfs(node.right, current_sum)
            
            # Remove the current prefix sum count as we are backtracking
            prefix_sum_count[current_sum] -= 1
            
            # Return the total number of paths
            return paths_ending_here + paths_from_left + paths_from_right
        
        # Start the DFS from the root with an initial sum of 0
        return dfs(root, 0)

def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
    return Solution().pathSum(root, targetSum)