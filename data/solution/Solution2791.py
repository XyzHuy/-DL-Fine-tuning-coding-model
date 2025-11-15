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
from collections import defaultdict, Counter
from typing import List

class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        def dfs(node, mask):
            # Add the current bitmask to the count
            counts[mask] += 1
            
            # Explore children
            for neighbor in graph[node]:
                # Calculate the new bitmask for the neighbor
                new_mask = mask ^ (1 << (ord(s[neighbor]) - ord('a')))
                # Update the result with the number of valid pairs ending at this neighbor
                result[0] += counts[new_mask]
                for i in range(26):
                    # Check for pairs with one character having odd frequency
                    result[0] += counts[new_mask ^ (1 << i)]
                # Recur for the child
                dfs(neighbor, new_mask)
        
        n = len(parent)
        # Build the graph
        graph = defaultdict(list)
        for i in range(1, n):
            graph[parent[i]].append(i)
        
        # Initialize bitmask counts and result
        counts = Counter()
        result = [0]
        
        # Start DFS from the root node (0)
        dfs(0, 0)
        
        return result[0]

# Example usage:
# sol = Solution()
# print(sol.countPalindromePaths([-1,0,0,1,1,2], "acaabc"))  # Output: 8
# print(sol.countPalindromePaths([-1,0,0,0,0], "aaaaa"))    # Output: 10

def countPalindromePaths(parent: List[int], s: str) -> int:
    return Solution().countPalindromePaths(parent, s)