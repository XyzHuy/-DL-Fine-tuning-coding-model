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
    def deleteDuplicatesUnsorted(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # First pass: count the occurrences of each value
        value_counts = {}
        current = head
        while current:
            if current.val in value_counts:
                value_counts[current.val] += 1
            else:
                value_counts[current.val] = 1
            current = current.next
        
        # Second pass: build the new list with only unique values
        dummy = ListNode(0)
        tail = dummy
        current = head
        while current:
            if value_counts[current.val] == 1:
                tail.next = current
                tail = tail.next
            current = current.next
        
        # Terminate the new list
        tail.next = None
        
        return dummy.next

def deleteDuplicatesUnsorted(head: Optional[ListNode]) -> Optional[ListNode]:
    return Solution().deleteDuplicatesUnsorted(head)