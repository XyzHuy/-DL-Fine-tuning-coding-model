# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



node = None

def sortedListToBST( head):
    global node
    # Bottom-up recursion O(n) and O(lgn)
    if head is None:
        return head
    size = 0
    pos = node = head
    while pos is not None:
        pos = pos.next
        size += 1
    return inorderHelper(0, size - 1)

def inorderHelper( start, end):
    global node
    if start > end:
        return None
    mid = (start + end) / 2
    # left side and move
    left = inorderHelper(start, mid - 1)
    # move and create
    root = TreeNode(node.val)
    root.left = left
    node = node.next
    # right side and move
    root.right = inorderHelper(mid + 1, end)
    return root