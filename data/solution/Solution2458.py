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
from typing import List, Optional

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depth = {}  # Maps node value to its depth
        subtree_height = {}  # Maps node value to its subtree height
        level_max_heights = {}  # Maps level to a sorted list of (height, node value) tuples

        def dfs(node, current_depth):
            if not node:
                return 0
            depth[node.val] = current_depth
            left_height = dfs(node.left, current_depth + 1)
            right_height = dfs(node.right, current_depth + 1)
            subtree_height[node.val] = 1 + max(left_height, right_height)
            
            level = current_depth
            if level not in level_max_heights:
                level_max_heights[level] = []
            level_max_heights[level].append((subtree_height[node.val], node.val))
            level_max_heights[level].sort(reverse=True)
            if len(level_max_heights[level]) > 2:
                level_max_heights[level].pop()
            
            return subtree_height[node.val]
        
        dfs(root, 0)
        
        max_height = subtree_height[root.val] - 1
        
        answer = []
        for query in queries:
            node_depth = depth[query]
            if node_depth == 0:
                # Removing the root
                answer.append(0)
                continue
            
            level = node_depth
            if len(level_max_heights[level]) == 1:
                # Only one node at this level, removing it will reduce the height by the height of this node
                answer.append(node_depth - 1)
            else:
                # There are at least two nodes at this level
                if level_max_heights[level][0][1] == query:
                    # The node to be removed is the tallest, use the second tallest
                    answer.append(node_depth - 1 + level_max_heights[level][1][0])
                else:
                    # The node to be removed is not the tallest, use the tallest
                    answer.append(node_depth - 1 + level_max_heights[level][0][0])
        
        return answer

def treeQueries(root: Optional[TreeNode], queries: List[int]) -> List[int]:
    return Solution().treeQueries(root, queries)