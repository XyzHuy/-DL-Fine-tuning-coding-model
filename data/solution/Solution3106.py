import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        # Helper function to calculate the minimum distance between two characters in a cyclic order
        def min_distance(c1, c2):
            d1 = abs(ord(c1) - ord(c2))
            d2 = 26 - d1
            return min(d1, d2)
        
        # Convert the string to a list of characters for easier manipulation
        t = list(s)
        
        # Iterate over each character in the string
        for i in range(len(t)):
            if k == 0:
                break
            
            # Calculate the distance to 'a'
            dist_to_a = min_distance(t[i], 'a')
            
            # If we can change the current character to 'a' without exceeding k, do it
            if dist_to_a <= k:
                t[i] = 'a'
                k -= dist_to_a
            else:
                # Otherwise, change the character as much as possible within the remaining k
                t[i] = chr(ord(t[i]) - k)
                k = 0
        
        # Join the list back into a string and return
        return ''.join(t)

def getSmallestString(s: str, k: int) -> str:
    return Solution().getSmallestString(s, k)