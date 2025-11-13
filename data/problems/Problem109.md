Given a binary tree, determine if it is height-balanced.
 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true

 
Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104


Boilerplate code:
```python
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isBalanced(root):
    ...
```
