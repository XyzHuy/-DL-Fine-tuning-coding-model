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
    def gameResult(self, head: Optional[ListNode]) -> str:
        even_points = 0
        odd_points = 0
        
        current = head
        
        while current and current.next:
            even_value = current.val
            odd_value = current.next.val
            
            if even_value > odd_value:
                even_points += 1
            elif odd_value > even_value:
                odd_points += 1
            
            # Move to the next pair
            current = current.next.next
        
        if even_points > odd_points:
            return "Even"
        elif odd_points > even_points:
            return "Odd"
        else:
            return "Tie"

def gameResult(head: Optional[ListNode]) -> str:
    return Solution().gameResult(head)