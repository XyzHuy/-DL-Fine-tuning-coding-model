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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        # Queue for level order traversal
        queue = deque([root])
        level = 0
        
        while queue:
            level_size = len(queue)
            nodes_to_reverse = []
            
            for _ in range(level_size):
                node = queue.popleft()
                
                if level % 2 == 1:
                    nodes_to_reverse.append(node)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse the node values at the current odd level
            if level % 2 == 1:
                for i in range(len(nodes_to_reverse) // 2):
                    nodes_to_reverse[i].val, nodes_to_reverse[~i].val = nodes_to_reverse[~i].val, nodes_to_reverse[i].val
            
            level += 1
        
        return root

def reverseOddLevels(root: Optional[TreeNode]) -> Optional[TreeNode]:
    return Solution().reverseOddLevels(root)