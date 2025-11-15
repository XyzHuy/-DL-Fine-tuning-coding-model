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
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # Initialize the result variable to 0
        result = 0
        
        # Traverse the linked list
        current = head
        while current:
            # Shift the current result to the left by 1 (equivalent to multiplying by 2)
            # and add the current node's value
            result = (result << 1) | current.val
            # Move to the next node
            current = current.next
        
        return result

def getDecimalValue(head: Optional[ListNode]) -> int:
    return Solution().getDecimalValue(head)