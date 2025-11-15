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
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Helper function to reverse the linked list
        def reverseList(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev
        
        # Reverse the linked list to facilitate addition from least significant digit
        head = reverseList(head)
        
        carry = 0
        current = head
        prev = None
        
        # Traverse the list and double each digit
        while current or carry:
            # Calculate the new value and carry
            new_val = (current.val * 2 if current else 0) + carry
            carry = new_val // 10
            new_val %= 10
            
            # Update the current node's value
            if current:
                current.val = new_val
                prev = current
                current = current.next
            else:
                # If there's a carry left after the last node, add a new node
                prev.next = ListNode(new_val)
                break
        
        # Reverse the list back to original order
        return reverseList(head)

def doubleIt(head: Optional[ListNode]) -> Optional[ListNode]:
    return Solution().doubleIt(head)