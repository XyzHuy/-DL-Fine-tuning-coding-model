Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

Example:
Input: [1,2,3,4,5]

Output: return the root of the binary tree [4,5,2,#,#,3,1]


Boilerplate code:
```python
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def upsideDownBinaryTree(root):
    ...
```
