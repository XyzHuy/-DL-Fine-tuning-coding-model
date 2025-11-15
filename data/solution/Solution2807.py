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
import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            # Calculate the greatest common divisor of the current node and the next node
            gcd_value = math.gcd(current.val, current.next.val)
            # Create a new node with the gcd_value
            new_node = ListNode(gcd_value, current.next)
            # Insert the new node between the current node and the next node
            current.next = new_node
            # Move to the node after the new node
            current = new_node.next
        return head

def insertGreatestCommonDivisors(head: Optional[ListNode]) -> Optional[ListNode]:
    return Solution().insertGreatestCommonDivisors(head)