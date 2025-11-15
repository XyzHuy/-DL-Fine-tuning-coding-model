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
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums to a set for O(1) look-up times
        nums_set = set(nums)
        
        # Create a dummy node to handle edge cases where the head needs to be removed
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Traverse the linked list
        while current.next:
            # If the next node's value is in nums_set, skip it
            if current.next.val in nums_set:
                current.next = current.next.next
            else:
                # Otherwise, move to the next node
                current = current.next
        
        # Return the modified list, which starts at dummy.next
        return dummy.next

def modifiedList(nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    return Solution().modifiedList(nums, head)