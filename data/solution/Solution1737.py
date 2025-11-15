import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        # Count the frequency of each character in both strings
        count_a = [0] * 26
        count_b = [0] * 26
        
        for char in a:
            count_a[ord(char) - ord('a')] += 1
            
        for char in b:
            count_b[ord(char) - ord('a')] += 1
            
        total_operations = float('inf')
        n = len(a)
        m = len(b)
        
        # Condition 3: Both a and b consist of only one distinct letter
        for i in range(26):
            total_operations = min(total_operations, n + m - count_a[i] - count_b[i])
        
        # Condition 1 and 2: Every letter in a is strictly less than every letter in b or vice versa
        prefix_a = 0
        prefix_b = 0
        
        for i in range(25):  # We don't need to check for 'z' as there is no character after 'z'
            prefix_a += count_a[i]
            prefix_b += count_b[i]
            
            # Calculate operations needed for condition 1: all characters in a < all characters in b
            operations_1 = prefix_a + (m - prefix_b)
            
            # Calculate operations needed for condition 2: all characters in b < all characters in a
            operations_2 = prefix_b + (n - prefix_a)
            
            total_operations = min(total_operations, operations_1, operations_2)
        
        return total_operations

def minCharacters(a: str, b: str) -> int:
    return Solution().minCharacters(a, b)