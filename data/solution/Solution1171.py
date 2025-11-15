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
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases easily
        dummy = ListNode(0)
        dummy.next = head
        
        # Dictionary to store prefix sum and its corresponding node
        prefix_sum = 0
        sum_map = {0: dummy}
        
        # Traverse the linked list to calculate prefix sums
        current = head
        while current:
            prefix_sum += current.val
            sum_map[prefix_sum] = current
            current = current.next
        
        # Reset prefix sum and traverse the list again to set next pointers
        prefix_sum = 0
        current = dummy
        while current:
            prefix_sum += current.val
            current.next = sum_map[prefix_sum].next
            current = current.next
        
        return dummy.next

def removeZeroSumSublists(head: Optional[ListNode]) -> Optional[ListNode]:
    return Solution().removeZeroSumSublists(head)