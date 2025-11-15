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
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to help with the result list
        dummy = ListNode(0)
        current = dummy
        sum_of_nodes = 0
        
        # Traverse the linked list starting from the first node after the initial 0
        head = head.next
        
        while head:
            if head.val == 0:
                # When a 0 is encountered, create a new node with the accumulated sum
                current.next = ListNode(sum_of_nodes)
                current = current.next
                sum_of_nodes = 0
            else:
                # Accumulate the sum of nodes between zeros
                sum_of_nodes += head.val
            head = head.next
        
        return dummy.next

def mergeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    return Solution().mergeNodes(head)