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
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # To form a valid binary tree, there must be exactly one root node (in-degree 0)
        # and all other nodes must have exactly one parent (in-degree 1).
        # Additionally, the tree must be connected and acyclic.

        # Step 1: Calculate in-degrees for each node
        in_degree = [0] * n
        for i in range(n):
            if leftChild[i] != -1:
                in_degree[leftChild[i]] += 1
            if rightChild[i] != -1:
                in_degree[rightChild[i]] += 1

        # Step 2: Find the root (node with in-degree 0)
        root_candidates = [i for i in range(n) if in_degree[i] == 0]
        
        # There must be exactly one root
        if len(root_candidates) != 1:
            return False

        # Step 3: Perform a DFS to check if the graph is connected and acyclic
        def dfs(node, visited):
            if node == -1:
                return True
            if visited[node]:
                return False  # Cycle detected
            visited[node] = True
            return dfs(leftChild[node], visited) and dfs(rightChild[node], visited)

        root = root_candidates[0]
        visited = [False] * n
        if not dfs(root, visited):
            return False  # Cycle detected or disconnected graph

        # Step 4: Ensure all nodes are visited (graph is connected)
        return all(visited)

def validateBinaryTreeNodes(n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    return Solution().validateBinaryTreeNodes(n, leftChild, rightChild)