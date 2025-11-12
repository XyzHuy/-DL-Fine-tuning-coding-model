# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    n = len(inorder)
    inOrderMap = {inorder[i]: i for i in range(n)}
    return buildTreeUtil(preorder, inorder, inOrderMap, 0, n - 1, 0, n - 1)

def buildTreeUtil(preorder, inorder, inOrderMap, pStart, pEnd, iStart, iEnd):
    if pStart > pEnd or iStart > iEnd:
        return None
    root = TreeNode(preorder[pStart])
    rootIdx = inOrderMap[root.val]
    root.left = buildTreeUtil(preorder, inorder, inOrderMap, pStart + 1, pStart + rootIdx - iStart + 1, iStart,
                                    rootIdx - 1)
    root.right = buildTreeUtil(preorder, inorder, inOrderMap, pStart + rootIdx - iStart + 1, pEnd, rootIdx + 1,
                                    iEnd)
    return root