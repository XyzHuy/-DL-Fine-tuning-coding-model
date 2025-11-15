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
from typing import List

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        # Step 1: Create a parent mapping
        parent = {}
        for region_list in regions:
            for region in region_list[1:]:
                parent[region] = region_list[0]
        
        # Step 2: Trace the path from region1 to the root
        ancestors = set()
        while region1 in parent:
            ancestors.add(region1)
            region1 = parent[region1]
        ancestors.add(region1)  # Add the root itself
        
        # Step 3: Trace the path from region2 to the root and find the common ancestor
        while region2 not in ancestors:
            region2 = parent[region2]
        
        return region2

# Example usage:
# sol = Solution()
# regions = [["Earth", "North America", "South America"], ["North America", "United States", "Canada"], ["United States", "New York", "Boston"], ["Canada", "Ontario", "Quebec"], ["South America", "Brazil"]]
# region1 = "Quebec"
# region2 = "New York"
# print(sol.findSmallestRegion(regions, region1, region2))  # Output: "North America"

def findSmallestRegion(regions: List[List[str]], region1: str, region2: str) -> str:
    return Solution().findSmallestRegion(regions, region1, region2)