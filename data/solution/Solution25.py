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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(start, end):
            prev, curr = None, start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        # Create a dummy node to handle edge cases more easily
        dummy = ListNode(0)
        dummy.next = head
        before = dummy
        after = head
        
        while after:
            count = 0
            # Check if there are at least k nodes left in the list
            while after and count < k:
                after = after.next
                count += 1
            
            # If there are less than k nodes, we are done
            if count < k:
                break
            
            # Reverse the k nodes
            last_in_reversed = before.next
            new_end = after
            new_start = reverseLinkedList(before.next, after)
            
            # Connect the reversed segment with the rest of the list
            before.next = new_start
            last_in_reversed.next = new_end
            
            # Move the pointers for the next iteration
            before = last_in_reversed
        
        return dummy.next

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    return Solution().reverseKGroup(head, k)