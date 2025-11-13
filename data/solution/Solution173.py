# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    # recursion
    # simple recursively without extra space
    if head is None or head.next is None:
        return head
    p = reverseList(head.next)
    head.next.next = head
    head.next = None
    return p
