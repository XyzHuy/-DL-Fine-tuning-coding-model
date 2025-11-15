import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def splitString(self, s: str) -> bool:
        
        def can_split(index, prev_num, parts_count):
            # If we reached the end of the string and have more than one part, return True
            if index == len(s):
                return parts_count > 1
            
            for i in range(index, len(s)):
                # Get the current number from the substring
                current_num = int(s[index:i+1])
                
                # Check if it's the first part or if it's one less than the previous part
                if parts_count == 0 or current_num == prev_num - 1:
                    # Recursively check the rest of the string
                    if can_split(i + 1, current_num, parts_count + 1):
                        return True
            
            return False
        
        return can_split(0, -1, 0)

def splitString(s: str) -> bool:
    return Solution().splitString(s)