import heapq
import itertools
from sortedcontainers import SortedList
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
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Initialize two pointers for both lists
        pointerA = headA
        pointerB = headB
        
        # Traverse both lists
        while pointerA is not pointerB:
            # Move pointerA to the head of list B if it reaches the end of list A
            if pointerA is None:
                pointerA = headB
            else:
                pointerA = pointerA.next
            
            # Move pointerB to the head of list A if it reaches the end of list B
            if pointerB is None:
                pointerB = headA
            else:
                pointerB = pointerB.next
        
        # Either both pointers meet at the intersection node or both become None
        return pointerA

def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    return Solution().getIntersectionNode(headA, headB)