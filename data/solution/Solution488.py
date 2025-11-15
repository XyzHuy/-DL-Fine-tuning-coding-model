import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        from collections import Counter
        
        def clean(board):
            stack = []
            for ball in board:
                if stack and stack[-1][0] != ball and stack[-1][1] >= 3:
                    stack.pop()
                if not stack or stack[-1][0] != ball:
                    stack.append([ball, 1])
                else:
                    stack[-1][1] += 1
            if stack and stack[-1][1] >= 3:
                stack.pop()
            return ''.join(ball * count for ball, count in stack)
        
        def dfs(board, hand_counter):
            if not board:
                return 0
            res, i = float("inf"), 0
            while i < len(board):
                j = i + 1
                while j < len(board) and board[i] == board[j]:
                    j += 1
                incr = 3 - (j - i)
                if hand_counter[board[i]] >= incr:
                    incr = 0 if incr < 0 else incr
                    hand_counter[board[i]] -= incr
                    temp = dfs(clean(board[:i] + board[j:]), hand_counter)
                    if temp >= 0:
                        res = min(res, temp + incr)
                    hand_counter[board[i]] += incr
                i = j
            return res if res != float("inf") else -1
        
        return dfs(board, Counter(hand))

def findMinStep(board: str, hand: str) -> int:
    return Solution().findMinStep(board, hand)