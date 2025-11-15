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
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases easily
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Find the kth node from the beginning
        for _ in range(k):
            current = current.next
        first_kth = current
        
        # Find the kth node from the end
        right = dummy
        while current:
            current = current.next
            right = right.next
        second_kth = right
        
        # Swap the values of the kth node from the beginning and the kth node from the end
        first_kth.val, second_kth.val = second_kth.val, first_kth.val
        
        return dummy.next

def swapNodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    return Solution().swapNodes(head, k)