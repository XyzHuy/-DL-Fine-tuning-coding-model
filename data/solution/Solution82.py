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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node that points to the head of the list
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:
            # If the next node and the node after that have the same value
            if current.next.val == current.next.next.val:
                # Find the last node that has the same value as the current duplicate
                duplicate_val = current.next.val
                while current.next and current.next.val == duplicate_val:
                    current.next = current.next.next
            else:
                # Move to the next node if no duplicate is found
                current = current.next
        
        # Return the list starting from the node after the dummy
        return dummy.next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    return Solution().deleteDuplicates(head)