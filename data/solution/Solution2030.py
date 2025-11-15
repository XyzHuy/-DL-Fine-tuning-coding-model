import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        n = len(s)
        # Count the occurrences of the target letter
        letter_count = s.count(letter)
        stack = []
        
        for i, char in enumerate(s):
            # While we can still form a valid subsequence and the current character
            # is lexicographically smaller than the top of the stack, we might want to
            # remove the top of the stack to make the subsequence smaller.
            while stack and len(stack) + n - i > k and char < stack[-1]:
                # If removing the top character would make it impossible to include
                # enough target letters, we cannot pop it.
                if stack[-1] == letter and letter_count <= repetition:
                    break
                # If the top character is the target letter, we decrease the count.
                if stack[-1] == letter:
                    repetition += 1
                stack.pop()
            
            # If adding the current character would not exceed the length k and
            # we can still meet the repetition requirement, we add it to the stack.
            if len(stack) < k:
                if char == letter:
                    stack.append(char)
                    repetition -= 1
                elif k - len(stack) > repetition:
                    stack.append(char)
                letter_count -= (char == letter)
        
        return ''.join(stack)

def smallestSubsequence(s: str, k: int, letter: str, repetition: int) -> str:
    return Solution().smallestSubsequence(s, k, letter, repetition)