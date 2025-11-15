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
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        current = head
        
        while current:
            # Keep the first m nodes
            for _ in range(m - 1):
                if not current:
                    break
                current = current.next
            
            # If we have reached the end, break
            if not current:
                break
            
            # Remove the next n nodes
            next_node = current
            for _ in range(n + 1):
                if not next_node:
                    break
                next_node = next_node.next
            
            current.next = next_node
            current = next_node
        
        return head

def deleteNodes(head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
    return Solution().deleteNodes(head, m, n)