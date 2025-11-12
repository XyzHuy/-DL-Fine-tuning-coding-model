# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # Two points
    try:
        fast = head.next.next
        slow = head.next

        while fast != slow:
            fast = fast.next.next
            slow = slow.next
    except:
        return None
    slow = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast
