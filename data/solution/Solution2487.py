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
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize an empty stack to keep track of nodes
        stack = []
        
        # Traverse the linked list
        current = head
        while current:
            # While stack is not empty and current node's value is greater than the value of the node at the top of the stack
            while stack and current.val > stack[-1].val:
                stack.pop()
            # Push the current node onto the stack
            stack.append(current)
            current = current.next
        
        # Reconstruct the linked list from the stack
        # The stack now contains the nodes of the modified list in the correct order
        dummy = ListNode(0)
        current = dummy
        for node in stack:
            current.next = node
            current = current.next
        
        # The next of the last node should be None
        current.next = None
        
        return dummy.next

def removeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    return Solution().removeNodes(head)