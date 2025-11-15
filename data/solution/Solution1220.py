import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Initialize the count of strings ending with each vowel for length 1
        a, e, i, o, u = 1, 1, 1, 1, 1
        
        for _ in range(1, n):
            # Calculate the count of strings of length _+1 ending with each vowel
            a_next = e
            e_next = (a + i) % MOD
            i_next = (a + e + o + u) % MOD
            o_next = (i + u) % MOD
            u_next = a
            
            # Update the counts for the next iteration
            a, e, i, o, u = a_next, e_next, i_next, o_next, u_next
        
        # The result is the sum of all counts for strings of length n
        return (a + e + i + o + u) % MOD

def countVowelPermutation(n: int) -> int:
    return Solution().countVowelPermutation(n)