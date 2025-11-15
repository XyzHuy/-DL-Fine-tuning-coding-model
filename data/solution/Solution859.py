import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # If lengths are not equal, we cannot make them equal by swapping
        if len(s) != len(goal):
            return False
        
        # If s and goal are already equal, check if there is any duplicate character in s
        if s == goal:
            # If there is a duplicate, we can swap them to keep the string the same
            return len(set(s)) < len(s)
        
        # Find the positions where s and goal differ
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        
        # We can only make them equal by swapping if there are exactly two differences
        if len(diff) != 2:
            return False
        
        # Check if swapping the differing positions makes the strings equal
        return s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]

def buddyStrings(s: str, goal: str) -> bool:
    return Solution().buddyStrings(s, goal)