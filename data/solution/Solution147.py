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
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Create a dummy node to act as the new head of the sorted list
        dummy = ListNode(0)
        dummy.next = head
        current = head.next
        prev = head
        
        while current:
            # If the current node is in the correct position, move on
            if current.val >= prev.val:
                prev = current
                current = current.next
            else:
                # Otherwise, find the correct position for the current node
                temp = dummy
                while temp.next and temp.next.val < current.val:
                    temp = temp.next
                
                # Insert the current node in the correct position
                prev.next = current.next
                current.next = temp.next
                temp.next = current
                
                # Move to the next node
                current = prev.next
        
        return dummy.next

def insertionSortList(head: Optional[ListNode]) -> Optional[ListNode]:
    return Solution().insertionSortList(head)