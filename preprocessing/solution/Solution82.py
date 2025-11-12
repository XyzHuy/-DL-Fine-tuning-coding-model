# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates( head):
    if head is None:
        return None
    pos = head
    while pos is not None and pos.next is not None:
        if pos.val == pos.next.val:
            pos.next = pos.next.next
        else:
            pos = pos.next
    return head
