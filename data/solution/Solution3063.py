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
from collections import Counter
from typing import Optional

class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Traverse the linked list and count the frequency of each element
        frequency_counter = Counter()
        current = head
        while current:
            frequency_counter[current.val] += 1
            current = current.next
        
        # Create a new linked list from the frequency values
        prev = None
        for frequency in frequency_counter.values():
            new_node = ListNode(frequency)
            new_node.next = prev
            prev = new_node
        
        return prev

def frequenciesOfElements(head: Optional[ListNode]) -> Optional[ListNode]:
    return Solution().frequenciesOfElements(head)