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
class Solution:
    def numTrees(self, n: int) -> int:
        # This problem can be solved using dynamic programming.
        # The idea is to use the concept of Catalan numbers.
        # G(n) = sum(G(i-1) * G(n-i)) for i in range(1, n+1)
        # where G(n) is the number of unique BSTs with n nodes.
        
        # Base case: There is one unique BST with 0 nodes and one with 1 node
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1
        
        # Calculate the number of unique BSTs for each number of nodes from 2 to n
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        
        return G[n]

def numTrees(n: int) -> int:
    return Solution().numTrees(n)