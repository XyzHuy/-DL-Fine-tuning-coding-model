# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums):
    # Recursion with index
    return getHelper(nums, 0, len(nums) - 1)

def getHelper(nums, start, end):
    if start > end:
        return None
    mid = (start + end) / 2
    node = TreeNode(nums[mid])
    node.left = getHelper(nums, start, mid - 1)
    node.right = getHelper(nums, mid + 1, end)
    return node