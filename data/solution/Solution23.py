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
import heapq
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Initialize a min-heap
        min_heap = []
        
        # Push the head of each list into the heap
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(min_heap, (lst.val, i, lst))
        
        # Dummy head to help easily return the merged list
        dummy = ListNode()
        current = dummy
        
        # While there are still nodes in the heap
        while min_heap:
            # Pop the smallest element from the heap
            val, i, node = heapq.heappop(min_heap)
            # Attach the smallest node to the merged list
            current.next = node
            current = current.next
            # If there is a next node in the same list, push it into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        # Return the merged list, which starts at dummy.next
        return dummy.next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    return Solution().mergeKLists(lists)