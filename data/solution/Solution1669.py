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
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Initialize pointers
        prev = None
        current = list1
        
        # Move current to the node just before the ath node
        for _ in range(a):
            prev = current
            current = current.next
        
        # prev now points to the (a-1)th node
        # current now points to the ath node
        
        # Move current to the bth node
        for _ in range(b - a + 1):
            current = current.next
        
        # current now points to the (b+1)th node
        
        # Connect the (a-1)th node to the head of list2
        prev.next = list2
        
        # Move to the end of list2
        while list2.next:
            list2 = list2.next
        
        # Connect the end of list2 to the (b+1)th node
        list2.next = current
        
        return list1

def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    return Solution().mergeInBetween(list1, a, b, list2)