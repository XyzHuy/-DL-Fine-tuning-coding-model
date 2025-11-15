import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        # Create a 2D array to store lengths of longest common subsequence
        f = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])
        
        # Reconstruct the shortest common supersequence
        ans = []
        i, j = m, n
        while i > 0 or j > 0:
            if i == 0:
                j -= 1
                ans.append(str2[j])
            elif j == 0:
                i -= 1
                ans.append(str1[i])
            else:
                if f[i][j] == f[i - 1][j]:
                    i -= 1
                    ans.append(str1[i])
                elif f[i][j] == f[i][j - 1]:
                    j -= 1
                    ans.append(str2[j])
                else:
                    i -= 1
                    j -= 1
                    ans.append(str1[i])
        
        # The answer is constructed in reverse order
        return ''.join(ans[::-1])

def shortestCommonSupersequence(str1: str, str2: str) -> str:
    return Solution().shortestCommonSupersequence(str1, str2)