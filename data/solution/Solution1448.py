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
class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            
            # Check if the current node is a good node
            is_good = 1 if node.val >= max_so_far else 0
            
            # Update the maximum value seen so far on the path
            new_max = max(max_so_far, node.val)
            
            # Recur for left and right subtrees
            good_in_left = dfs(node.left, new_max)
            good_in_right = dfs(node.right, new_max)
            
            # Return the total count of good nodes in the subtree rooted at the current node
            return is_good + good_in_left + good_in_right
        
        # Start the DFS with the root node and its value as the initial maximum
        return dfs(root, root.val)

def goodNodes(root: Optional[TreeNode]) -> int:
    return Solution().goodNodes(root)