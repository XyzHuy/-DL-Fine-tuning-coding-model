import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index, t_index = 0, 0
        s_len, t_len = len(s), len(t)
        
        while s_index < s_len and t_index < t_len:
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1
        
        return s_index == s_len

# For the follow-up question, if there are lots of incoming s strings to check against a single t string,
# we can preprocess t to make the checks more efficient. One way is to use a dictionary to store the indices
# of each character in t. This allows us to perform binary search to find the next valid index for each character
# in s, reducing the time complexity for each s from O(n) to O(m log n), where m is the length of s and n is the length of t.
# Here's how you can implement it:

import collections
import bisect

class SolutionFollowUp:
    def __init__(self, t: str):
        self.t_index_map = collections.defaultdict(list)
        for index, char in enumerate(t):
            self.t_index_map[char].append(index)

    def isSubsequence(self, s: str) -> bool:
        current_index = -1
        for char in s:
            if char not in self.t_index_map:
                return False
            # Use binary search to find the smallest index in t which is larger than current_index
            positions = self.t_index_map[char]
            index = bisect.bisect_right(positions, current_index)
            if index == len(positions):
                return False
            current_index = positions[index]
        return True

def isSubsequence(s: str, t: str) -> bool:
    return Solution().isSubsequence(s, t)