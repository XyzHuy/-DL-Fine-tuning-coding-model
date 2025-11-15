import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        from itertools import permutations
        
        # Convert the number to a list of characters for easier manipulation
        num_list = list(num)
        
        # Generate the k-th smallest permutation
        for _ in range(k):
            # Find the next permutation
            for i in range(len(num_list) - 2, -1, -1):
                if num_list[i] < num_list[i + 1]:
                    # Find the smallest number larger than num_list[i] to the right
                    for j in range(len(num_list) - 1, i, -1):
                        if num_list[j] > num_list[i]:
                            # Swap them
                            num_list[i], num_list[j] = num_list[j], num_list[i]
                            # Reverse the sequence after the original position of num_list[i]
                            num_list[i + 1:] = reversed(num_list[i + 1:])
                            break
                    break
        
        # Convert the target permutation back to a string
        target = ''.join(num_list)
        
        # Initialize variables to count the number of swaps
        swaps = 0
        num_list = list(num)  # Reset num_list to the original number
        
        # Use a two-pointer technique to count the minimum number of swaps
        for i in range(len(num_list)):
            if num_list[i] != target[i]:
                # Find the position of target[i] in the remaining part of num_list
                for j in range(i + 1, len(num_list)):
                    if num_list[j] == target[i]:
                        # Count the number of swaps needed to bring num_list[j] to position i
                        swaps += j - i
                        # Perform the swap by removing the element and inserting it at position i
                        num_list[i + 1:j + 1] = num_list[i:j]
                        break
        
        return swaps

def getMinSwaps(num: str, k: int) -> int:
    return Solution().getMinSwaps(num, k)