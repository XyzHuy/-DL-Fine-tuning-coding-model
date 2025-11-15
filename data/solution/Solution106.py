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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        # The last element in postorder is the root
        root_val = postorder[-1]
        root = TreeNode(root_val)
        
        # Find the index of the root in inorder list
        root_index = inorder.index(root_val)
        
        # Elements to the left of root_index in inorder list are part of left subtree
        # Elements to the right of root_index in inorder list are part of right subtree
        root.right = self.buildTree(inorder[root_index + 1:], postorder[root_index:-1])
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        
        return root

def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    return Solution().buildTree(inorder, postorder)