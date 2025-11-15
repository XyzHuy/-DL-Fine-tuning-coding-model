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
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Initialize the matrix with -1
        matrix = [[-1] * n for _ in range(m)]
        
        # Define the boundaries of the spiral
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        
        # Traverse the matrix in a spiral order
        while head and top <= bottom and left <= right:
            # Fill the top row
            for i in range(left, right + 1):
                if head:
                    matrix[top][i] = head.val
                    head = head.next
            top += 1
            
            # Fill the right column
            for i in range(top, bottom + 1):
                if head:
                    matrix[i][right] = head.val
                    head = head.next
            right -= 1
            
            # Fill the bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    if head:
                        matrix[bottom][i] = head.val
                        head = head.next
                bottom -= 1
            
            # Fill the left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    if head:
                        matrix[i][left] = head.val
                        head = head.next
                left += 1
        
        return matrix

def spiralMatrix(m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
    return Solution().spiralMatrix(m, n, head)