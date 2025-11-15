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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Helper function to get the length of a linked list
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        # Helper function to add nodes with the same length
        def add_nodes(node1, node2):
            if not node1 and not node2:
                return None, 0
            next_node, carry = add_nodes(node1.next, node2.next)
            total = node1.val + node2.val + carry
            current = ListNode(total % 10)
            current.next = next_node
            return current, total // 10
        
        # Get lengths of both lists
        len1, len2 = get_length(l1), get_length(l2)
        
        # Align the lists by padding the shorter list with zeros
        head1, head2 = l1, l2
        if len1 < len2:
            for _ in range(len2 - len1):
                head1 = ListNode(0, head1)
        else:
            for _ in range(len1 - len2):
                head2 = ListNode(0, head2)
        
        # Add the two lists
        result, carry = add_nodes(head1, head2)
        
        # If there's a carry left, add a new node at the beginning
        if carry:
            result = ListNode(carry, result)
        
        return result

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    return Solution().addTwoNumbers(l1, l2)