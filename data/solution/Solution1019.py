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
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # Convert linked list to array for easier manipulation
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        
        # Initialize the result array with zeros
        result = [0] * len(arr)
        # Stack to keep track of indices of the elements for which we haven't found the next greater element yet
        stack = []
        
        # Traverse the array
        for i in range(len(arr)):
            # While stack is not empty and the current element is greater than the element at the index stored in the stack
            while stack and arr[i] > arr[stack[-1]]:
                # Pop the index from the stack and update the result for that index
                index = stack.pop()
                result[index] = arr[i]
            # Push the current index to the stack
            stack.append(i)
        
        return result

def nextLargerNodes(head: Optional[ListNode]) -> List[int]:
    return Solution().nextLargerNodes(head)