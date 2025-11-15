import random
import functools
import collections
import string
import math
import datetime


from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Count the frequency of each character in t
        dict_t = Counter(t)
        
        # Number of unique characters in t that need to be in the window
        required = len(dict_t)
        
        # Left and right pointer
        l, r = 0, 0
        
        # Form a dictionary to keep a count of all the unique characters in the current window
        formed = 0
        
        # Dictionary which keeps a count of all the unique characters in the current window
        window_counts = {}
        
        # To store the result
        ans = float("inf"), None, None
        
        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            # Try and contract the window until it ceases to be 'desirable'
            while l <= r and formed == required:
                character = s[l]
                
                # Save the smallest window until now
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # The character at the position pointed by the `left` pointer is no longer a part of the window
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                
                # Move the left pointer ahead
                l += 1    
            
            # Keep expanding the window    
            r += 1    
        
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

def minWindow(s: str, t: str) -> str:
    return Solution().minWindow(s, t)