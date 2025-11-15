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
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        def is_prime(num):
            if num <= 1:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for i in range(3, int(num**0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True

        # Sieve of Eratosthenes to find all prime numbers up to n
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False
        for p in range(2, int(n**0.5) + 1):
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
        
        # Build the tree as an adjacency list
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        def dfs(u, parent):
            # Returns (count of non-prime nodes in the subtree, is_prime)
            if prime[u]:
                return (0, True)
            count = 1
            for v in tree[u]:
                if v != parent:
                    v_count, v_is_prime = dfs(v, u)
                    if not v_is_prime:
                        count += v_count
            return (count, False)
        
        def count_paths_from_prime(u):
            non_prime_counts = []
            total_paths = 0
            for v in tree[u]:
                if not prime[v]:
                    count, _ = dfs(v, u)
                    non_prime_counts.append(count)
                    total_paths += count
            # For each pair of non-prime counts, add to the result
            result = 0
            for i in range(len(non_prime_counts)):
                for j in range(i + 1, len(non_prime_counts)):
                    result += non_prime_counts[i] * non_prime_counts[j]
            # Add the paths that include the prime node and one non-prime path
            result += total_paths
            return result
        
        total_valid_paths = 0
        for i in range(1, n + 1):
            if prime[i]:
                total_valid_paths += count_paths_from_prime(i)
        
        return total_valid_paths

def countPaths(n: int, edges: List[List[int]]) -> int:
    return Solution().countPaths(n, edges)