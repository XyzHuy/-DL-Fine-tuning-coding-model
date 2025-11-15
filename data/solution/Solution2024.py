import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def f(c: str) -> int:
            cnt = l = 0
            for r in range(len(answerKey)):
                cnt += answerKey[r] == c
                if cnt > k:
                    cnt -= answerKey[l] == c
                    l += 1
            return len(answerKey) - l

        return max(f("T"), f("F"))

def maxConsecutiveAnswers(answerKey: str, k: int) -> int:
    return Solution().maxConsecutiveAnswers(answerKey, k)