import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s):
            return s == s[::-1]
        
        def to_base_k(num, base):
            if num == 0:
                return "0"
            digits = []
            while num:
                digits.append(int(num % base))
                num //= base
            return ''.join(str(x) for x in digits[::-1])
        
        def generate_palindromes(length):
            if length == 1:
                for i in range(1, 10):
                    yield i
            elif length == 2:
                for i in range(1, 10):
                    yield i * 11
            else:
                half_len = (length + 1) // 2
                start = 10**(half_len - 1)
                end = 10**half_len
                for i in range(start, end):
                    s = str(i)
                    if length % 2 == 0:
                        yield int(s + s[::-1])
                    else:
                        yield int(s + s[-2::-1])
        
        k_mirror_numbers = []
        length = 1
        while len(k_mirror_numbers) < n:
            for num in generate_palindromes(length):
                if is_palindrome(to_base_k(num, k)):
                    k_mirror_numbers.append(num)
                    if len(k_mirror_numbers) == n:
                        break
            length += 1
        
        return sum(k_mirror_numbers)

# Example usage:
# sol = Solution()
# print(sol.kMirror(2, 5))  # Output: 25
# print(sol.kMirror(3, 7))  # Output: 499
# print(sol.kMirror(7, 17)) # Output: 20379000

def kMirror(k: int, n: int) -> int:
    return Solution().kMirror(k, n)