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
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        left_boundary = []
        right_boundary = []
        leaves = []
        
        def is_leaf(node):
            return node and not node.left and not node.right
        
        def add_left_boundary(node):
            if not node or is_leaf(node):
                return
            left_boundary.append(node.val)
            if node.left:
                add_left_boundary(node.left)
            else:
                add_left_boundary(node.right)
        
        def add_right_boundary(node):
            if not node or is_leaf(node):
                return
            right_boundary.append(node.val)
            if node.right:
                add_right_boundary(node.right)
            else:
                add_right_boundary(node.left)
        
        def add_leaves(node):
            if not node:
                return
            if is_leaf(node):
                leaves.append(node.val)
            add_leaves(node.left)
            add_leaves(node.right)
        
        # Always add the root to the boundary
        boundary = [root.val]
        
        # Add left boundary nodes
        add_left_boundary(root.left)
        
        # Add leaves
        add_leaves(root.left)
        add_leaves(root.right)
        
        # Add right boundary nodes in reverse order
        add_right_boundary(root.right)
        boundary.extend(left_boundary)
        boundary.extend(leaves)
        boundary.extend(right_boundary[::-1])
        
        return boundary

def boundaryOfBinaryTree(root: Optional[TreeNode]) -> List[int]:
    return Solution().boundaryOfBinaryTree(root)