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
    def maxXor(self, n: int, edges: List[List[int]], values: List[int]) -> int:
        from collections import defaultdict
        from sortedcontainers import SortedList
        
        # Build the tree as an adjacency list
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        # Function to calculate subtree sums
        def dfs(node, parent):
            subtree_sum = values[node]
            for neighbor in tree[node]:
                if neighbor != parent:
                    subtree_sum += dfs(neighbor, node)
            subtree_sums[node] = subtree_sum
            return subtree_sum
        
        # Store the sums of all subtrees
        subtree_sums = [0] * n
        dfs(0, -1)
        
        # Function to find the maximum XOR pair from two sorted lists
        def max_xor_pair(list1, list2):
            max_xor = 0
            for x in list1:
                # We are looking for a number y in list2 such that x XOR y is maximized
                # This can be done by binary searching for the number that is the most different from x
                # which means finding the number with the most differing first bit with x starting from the MSB
                target = x ^ (1 << 40)  # Start with the highest bit, assuming max sum is less than 2^40
                pos = list2.bisect_left(target)
                for i in [pos - 1, pos, pos + 1]:
                    if 0 <= i < len(list2):
                        max_xor = max(max_xor, x ^ list2[i])
            return max_xor
        
        # Store the subtree sums in a sorted list
        sorted_sums = SortedList()
        
        # Traverse the tree in post-order and calculate max XOR for each node
        max_score = 0
        
        def post_order(node, parent):
            nonlocal max_score
            current_sum = subtree_sums[node]
            max_score = max(max_score, max_xor_pair(sorted_sums, SortedList([current_sum])))
            for neighbor in tree[node]:
                if neighbor != parent:
                    post_order(neighbor, node)
            sorted_sums.add(current_sum)
        
        post_order(0, -1)
        
        return max_score

def maxXor(n: int, edges: List[List[int]], values: List[int]) -> int:
    return Solution().maxXor(n, edges, values)