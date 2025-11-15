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
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # 0: Unmonitored
        # 1: Monitored by a child
        # 2: Has a camera

        def dfs(node):
            if not node:
                return 1, 0  # No need to monitor a non-existent node, no camera needed

            left_monitored, left_cameras = dfs(node.left)
            right_monitored, right_cameras = dfs(node.right)

            # If any child is unmonitored, we need a camera at this node
            if left_monitored == 0 or right_monitored == 0:
                return 2, left_cameras + right_cameras + 1

            # If any child has a camera, this node is monitored
            if left_monitored == 2 or right_monitored == 2:
                return 1, left_cameras + right_cameras

            # If both children are monitored but do not have cameras, this node is unmonitored
            return 0, left_cameras + right_cameras

        root_monitored, root_cameras = dfs(root)
        # If the root is unmonitored, we need an additional camera at the root
        return root_cameras + (1 if root_monitored == 0 else 0)

def minCameraCover(root: Optional[TreeNode]) -> int:
    return Solution().minCameraCover(root)