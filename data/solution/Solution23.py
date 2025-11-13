# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):
    # recursive
    if lists is None:
        return None
    elif len(lists) == 0:
        return None
    return mergeK(lists, 0, len(lists) - 1)

def mergeK(lists, low, high):
    if low == high:
        return lists[low]
    elif low + 1 == high:
        return mergeTwolists(lists[low], lists[high])
    mid = (low + high) / 2
    return mergeTwolists(mergeK(lists, low, mid), mergeK(lists, mid + 1, high))

def mergeTwolists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    head = curr = ListNode(-1)
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    if l1 is not None:
        curr.next = l1
    if l2 is not None:
        curr.next = l2
    return head.next

