# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

result = 0

def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: int
    """
    global result
    pathSumHelper(root, sum, 0, {0: 1})
    return result

def pathSumHelper(root, target, so_far, cache):
    global result
    if root:
        # complement == 1, root->curr path
        complement = so_far + root.val - target
        if complement in cache:
            # S->E path, sum(root->S)-sum(root->E) = target
            result += cache[complement]
        cache[so_far + root.val] = cache.get(so_far + root.val, 0) + 1
        pathSumHelper(root.left, target, so_far + root.val, cache)
        pathSumHelper(root.right, target, so_far + root.val, cache)
        cache[so_far + root.val] -= 1
    return