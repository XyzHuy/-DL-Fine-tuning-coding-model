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
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_sublist(prev, k):
            # Reverse k nodes starting from prev.next
            node1 = prev.next
            node2 = node1.next
            for _ in range(k - 1):
                node1.next = node2.next
                node2.next = prev.next
                prev.next = node2
                node2 = node1.next
            return node1

        dummy = ListNode(0, head)
        group = 1
        prev = dummy

        while True:
            k = 0
            node = prev
            # Determine the length of the current group
            for _ in range(group):
                if not node.next:
                    break
                node = node.next
                k += 1

            if k % 2 == 0:
                # Reverse if the group length is even
                prev = reverse_sublist(prev, k)
            else:
                # Move to the end of the current group
                for _ in range(k):
                    prev = prev.next

            if not prev.next:
                break

            group += 1

        return dummy.next

def reverseEvenLengthGroups(head: Optional[ListNode]) -> Optional[ListNode]:
    return Solution().reverseEvenLengthGroups(head)