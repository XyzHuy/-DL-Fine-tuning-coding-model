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

from typing import List

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        days = [0] * n
        
        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                days[i] = max(days[i] + 1, days[stack.pop()])
            stack.append(i)
        
        return max(days)

def totalSteps(nums: List[int]) -> int:
    return Solution().totalSteps(nums)