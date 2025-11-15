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
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Step 1: Perform an in-order traversal to get sorted node values
        def in_order_traversal(node):
            if not node:
                return []
            return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
        
        # Step 2: Build a balanced BST from sorted values
        def build_balanced_bst(sorted_values, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = TreeNode(sorted_values[mid])
            node.left = build_balanced_bst(sorted_values, start, mid - 1)
            node.right = build_balanced_bst(sorted_values, mid + 1, end)
            return node
        
        # Get sorted values from the original BST
        sorted_values = in_order_traversal(root)
        
        # Build and return the balanced BST
        return build_balanced_bst(sorted_values, 0, len(sorted_values) - 1)

def balanceBST(root: Optional[TreeNode]) -> Optional[TreeNode]:
    return Solution().balanceBST(root)