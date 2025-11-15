import collections
import string
import math
import datetime


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip any leading or trailing spaces from the string
        s = s.strip()
        # Split the string into words
        words = s.split(' ')
        # Return the length of the last word
        return len(words[-1])

def lengthOfLastWord(s: str) -> int:
    return Solution().lengthOfLastWord(s)