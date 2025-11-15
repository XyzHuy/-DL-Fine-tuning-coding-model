import collections
import string
import math
import datetime


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase
        s = s.lower()
        # Filter out non-alphanumeric characters
        filtered_chars = [char for char in s if char.isalnum()]
        # Join the characters to form the cleaned string
        cleaned_string = ''.join(filtered_chars)
        # Check if the cleaned string is a palindrome
        return cleaned_string == cleaned_string[::-1]

def isPalindrome(s: str) -> bool:
    return Solution().isPalindrome(s)