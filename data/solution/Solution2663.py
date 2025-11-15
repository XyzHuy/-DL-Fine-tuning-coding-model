import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        n = len(s)
        s = list(s)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        # Try to increment the string from the end to the beginning
        for i in range(n - 1, -1, -1):
            # Increment the character at the current position
            index = alphabet.index(s[i]) + 1
            while index < k:
                char = alphabet[index]
                # Check if the new character forms a palindrome with the previous characters
                if (i >= 1 and s[i - 1] == char) or (i >= 2 and s[i - 2] == char):
                    index += 1
                    continue
                # If the new character is valid, update the string and break the loop
                s[i] = char
                break
            else:
                # If no valid character is found, continue to the previous position
                continue
            
            # Fill the rest of the string with the smallest possible characters
            for j in range(i + 1, n):
                for char in alphabet[:k]:
                    if (j >= 1 and s[j - 1] == char) or (j >= 2 and s[j - 2] == char):
                        continue
                    s[j] = char
                    break
            
            # Return the resulting string
            return ''.join(s)
        
        # If no valid string is found, return an empty string
        return ''

def smallestBeautifulString(s: str, k: int) -> str:
    return Solution().smallestBeautifulString(s, k)