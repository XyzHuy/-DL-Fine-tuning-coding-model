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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative approach
        prev = None
        current = head
        while current:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the current node's pointer
            prev = current            # Move pointers one position ahead
            current = next_node
        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if head is empty or only one node, return it
        if not head or not head.next:
            return head
        # Recursively reverse the rest of the list
        new_head = self.reverseListRecursive(head.next)
        # Reverse the current node's pointer
        head.next.next = head
        head.next = None
        return new_head

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    return Solution().reverseList(head)