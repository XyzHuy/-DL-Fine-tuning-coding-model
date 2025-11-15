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
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        current = head.next
        next_node = head.next.next
        
        critical_points = []
        index = 2  # Starting index from the second node
        
        while next_node:
            if (current.val > prev.val and current.val > next_node.val) or \
               (current.val < prev.val and current.val < next_node.val):
                critical_points.append(index)
            
            prev = current
            current = next_node
            next_node = next_node.next
            index += 1
        
        if len(critical_points) < 2:
            return [-1, -1]
        
        min_distance = min(critical_points[i] - critical_points[i - 1] for i in range(1, len(critical_points)))
        max_distance = critical_points[-1] - critical_points[0]
        
        return [min_distance, max_distance]

def nodesBetweenCriticalPoints(head: Optional[ListNode]) -> List[int]:
    return Solution().nodesBetweenCriticalPoints(head)