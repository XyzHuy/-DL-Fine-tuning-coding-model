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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create two dummy nodes to start the two partitions
        before = ListNode(0)
        after = ListNode(0)
        
        # Pointers to the current end of the two partitions
        before_curr = before
        after_curr = after
        
        # Traverse the original list and partition the nodes
        while head:
            if head.val < x:
                before_curr.next = head
                before_curr = before_curr.next
            else:
                after_curr.next = head
                after_curr = after_curr.next
            head = head.next
        
        # Connect the two partitions
        before_curr.next = after.next
        # Terminate the list after the last node in the 'after' partition
        after_curr.next = None
        
        # The new head of the list is the next node of the 'before' dummy node
        return before.next

def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    return Solution().partition(head, x)