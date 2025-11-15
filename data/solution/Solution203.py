import random
import functools
import collections
import string
import math
import datetime


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_node(values: list):
    if not values:
        return None
    head = ListNode(values[0])
    p = head
    for val in values[1:]:
        node = ListNode(val)
        p.next = node
        p = node
    return head

def is_same_list(p1, p2):
    if p1 is None and p2 is None:
        return True
    if not p1 or not p2:
        return False
    return p1.val == p2.val and is_same_list(p1.next, p2.next)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head of the list
        dummy = ListNode(next=head)
        current = dummy
        
        # Traverse the list
        while current.next:
            if current.next.val == val:
                # Skip the node with the target value
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        # Return the new head of the list
        return dummy.next

def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    return Solution().removeElements(head, val)