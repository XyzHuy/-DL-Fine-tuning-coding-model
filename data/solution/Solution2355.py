import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        stack = []  # This will store indices of the books array
        dp = [0] * n  # dp[i] will store the maximum books we can take ending at index i

        for i in range(n):
            # Maintain the stack such that books[stack[-1]] - stack[-1] is less than books[i] - i
            while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
                stack.pop()
            
            if stack:
                j = stack[-1]
                # Calculate the number of books we can take from j+1 to i
                count = min(books[i], i - j)
                total_books = (books[i] + books[i] - count + 1) * count // 2
                dp[i] = total_books + dp[j]
            else:
                # If stack is empty, calculate the number of books we can take from 0 to i
                count = min(books[i], i + 1)
                dp[i] = (books[i] + books[i] - count + 1) * count // 2
            
            stack.append(i)
        
        return max(dp)

# Example usage:
# sol = Solution()
# print(sol.maximumBooks([8,5,2,7,9]))  # Output: 19
# print(sol.maximumBooks([7,0,3,4,5]))  # Output: 12
# print(sol.maximumBooks([8,2,3,7,3,4,0,1,4,3]))  # Output: 13

def maximumBooks(books: List[int]) -> int:
    return Solution().maximumBooks(books)