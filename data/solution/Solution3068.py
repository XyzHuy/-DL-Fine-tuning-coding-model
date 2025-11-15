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
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # Calculate the initial sum of nums
        initial_sum = sum(nums)
        
        # Calculate the potential gain for each node if we XOR it with k
        gains = [max(0, (num ^ k) - num) for num in nums]
        
        # Count how many nodes have a positive gain
        positive_gain_count = sum(1 for gain in gains if gain > 0)
        
        # Calculate the total possible gain
        total_gain = sum(gains)
        
        # If the number of nodes with positive gain is even, we can achieve the total gain
        # If it's odd, we might need to sacrifice the smallest gain to make it even
        if positive_gain_count % 2 == 0:
            return initial_sum + total_gain
        else:
            # Find the smallest absolute change (either positive or negative) when XORing with k
            min_abs_change = min(abs(num - (num ^ k)) for num in nums)
            return initial_sum + total_gain - min_abs_change

# Example usage:
# sol = Solution()
# print(sol.maximumValueSum([1, 2, 1], 3, [[0, 1], [0, 2]]))  # Output: 6
# print(sol.maximumValueSum([2, 3], 7, [[0, 1]]))  # Output: 9
# print(sol.maximumValueSum([7, 7, 7, 7, 7, 7], 3, [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]))  # Output: 42

def maximumValueSum(nums: List[int], k: int, edges: List[List[int]]) -> int:
    return Solution().maximumValueSum(nums, k, edges)