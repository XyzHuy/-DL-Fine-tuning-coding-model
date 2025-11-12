# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


result = -2147483647

def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    global result
    # return (root.val,left+root.val,right+root.val,left+right+root);
    self.getNodeMaxValue(root)
    return result

def getNodeMaxValue(self, node):
    global result
    if node is None:
        return 0
    lresult = self.getNodeMaxValue(node.left)
    rresult = self.getNodeMaxValue(node.right)
    result = max(lresult + rresult + node.val, result)
    ret = node.val + max(lresult, rresult)
    # if max left or right < 0 then return 0
    if ret > 0:
        return ret
    return 0