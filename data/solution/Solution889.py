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
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        
        # The first element in preorder is the root
        root = TreeNode(preorder[0])
        
        # If the list has only one element, return the root
        if len(preorder) == 1:
            return root
        
        # The second element in preorder is the left child of the root
        left_child_value = preorder[1]
        # Find the index of the left child in postorder
        left_child_index = postorder.index(left_child_value)
        
        # Elements between 0 and left_child_index + 1 in postorder are part of the left subtree
        left_postorder = postorder[:left_child_index + 1]
        # Elements from 1 to len(left_postorder) in preorder are part of the left subtree
        left_preorder = preorder[1:1 + len(left_postorder)]
        
        # Remaining elements in preorder and postorder are part of the right subtree
        right_preorder = preorder[1 + len(left_postorder):]
        right_postorder = postorder[left_child_index + 1:-1]
        
        # Recursively construct the left and right subtrees
        root.left = self.constructFromPrePost(left_preorder, left_postorder)
        root.right = self.constructFromPrePost(right_preorder, right_postorder)
        
        return root

def constructFromPrePost(preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    return Solution().constructFromPrePost(preorder, postorder)