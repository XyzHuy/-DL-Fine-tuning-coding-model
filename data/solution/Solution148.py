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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Find the middle of the list
        middle = self.getMiddle(head)
        next_to_middle = middle.next
        middle.next = None
        
        # Recursively sort the two halves
        left = self.sortList(head)
        right = self.sortList(next_to_middle)
        
        # Merge the sorted halves
        sorted_list = self.sortedMerge(left, right)
        
        return sorted_list
    
    def getMiddle(self, head):
        if not head:
            return head
        
        slow = head
        fast = head.next
        
        while fast:
            fast = fast.next
            if fast:
                slow = slow.next
                fast = fast.next
        
        return slow
    
    def sortedMerge(self, a, b):
        result = None
        
        if not a:
            return b
        if not b:
            return a
        
        if a.val <= b.val:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        
        return result

def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    return Solution().sortList(head)