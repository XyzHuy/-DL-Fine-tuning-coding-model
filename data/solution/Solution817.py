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
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_set = set(nums)
        connected_components = 0
        in_component = False
        
        current = head
        while current:
            if current.val in num_set:
                if not in_component:
                    # Start of a new component
                    connected_components += 1
                    in_component = True
            else:
                in_component = False
            
            current = current.next
        
        return connected_components

def numComponents(head: Optional[ListNode], nums: List[int]) -> int:
    return Solution().numComponents(head, nums)