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
from math import comb
from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def count_ways(arr):
            if len(arr) <= 1:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            ways_left = count_ways(left)
            ways_right = count_ways(right)
            total_ways = comb(len(left) + len(right), len(left)) * ways_left * ways_right
            return total_ways
        
        # Subtract 1 to exclude the original permutation
        return (count_ways(nums) - 1) % (10**9 + 7)

# Example usage:
# sol = Solution()
# print(sol.numOfWays([2, 1, 3]))  # Output: 1
# print(sol.numOfWays([3, 4, 5, 1, 2]))  # Output: 5
# print(sol.numOfWays([1, 2, 3]))  # Output: 0

def numOfWays(nums: List[int]) -> int:
    return Solution().numOfWays(nums)