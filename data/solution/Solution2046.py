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
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Initialize pointers
        prev = None
        current = head
        
        while current:
            # If current node is negative, move it to the front
            if current.val < 0:
                if prev:
                    # Detach the current node from the list
                    prev.next = current.next
                    # Prepend the current node to the head
                    current.next = head
                    head = current
                    # Move current to the next node after prev
                    current = prev.next
                else:
                    # If prev is None, it means current is head and it's negative
                    # Just move to the next node
                    prev = current
                    current = current.next
            else:
                # Move both pointers forward
                prev = current
                current = current.next
        
        return head

def sortLinkedList(head: Optional[ListNode]) -> Optional[ListNode]:
    return Solution().sortLinkedList(head)