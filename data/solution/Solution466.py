import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if not s1 or not s2 or n1 == 0 or n2 == 0:
            return 0

        # To store the number of times s2 is matched and the corresponding position in s2
        index_map = {}
        count1, count2, index = 0, 0, 0

        # Run until we either run out of s1 or find a cycle
        while count1 < n1:
            # Iterate over s1
            for char in s1:
                if char == s2[index]:
                    index += 1
                    # If we have matched the whole s2, reset index and increase count2
                    if index == len(s2):
                        index = 0
                        count2 += 1
            # Increase the count of how many times we have concatenated s1
            count1 += 1

            # Check if we have seen this index before to detect a cycle
            if index in index_map:
                # We have found a cycle
                prev_count1, prev_count2 = index_map[index]
                pattern_count1 = count1 - prev_count1
                pattern_count2 = count2 - prev_count2

                # Calculate the number of complete cycles that can fit
                complete_cycles = (n1 - prev_count1) // pattern_count1
                count2 = prev_count2 + complete_cycles * pattern_count2
                count1 = prev_count1 + complete_cycles * pattern_count1

                # Break the loop if no more complete cycles can fit
                if count1 >= n1:
                    break
            else:
                # Store the current index and the counts in the map
                index_map[index] = (count1, count2)

        # Calculate how many times str2 can be formed from str1
        return count2 // n2

def getMaxRepetitions(s1: str, n1: int, s2: str, n2: int) -> int:
    return Solution().getMaxRepetitions(s1, n1, s2, n2)