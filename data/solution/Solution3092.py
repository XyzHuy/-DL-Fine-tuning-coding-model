import random
import functools
import collections
import string
import math
import datetime


from sortedcontainers import SortedList
from typing import List

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        # Dictionary to store the frequency of each ID
        id_freq = {}
        # SortedList to maintain the frequencies in sorted order
        freq_list = SortedList()
        # Result list to store the most frequent ID count after each step
        ans = []
        
        for i in range(len(nums)):
            num = nums[i]
            change = freq[i]
            
            # If the ID is already in the dictionary, remove its current frequency from the SortedList
            if num in id_freq:
                current_freq = id_freq[num]
                freq_list.remove(current_freq)
            else:
                current_freq = 0
            
            # Update the frequency of the ID
            new_freq = current_freq + change
            id_freq[num] = new_freq
            
            # Add the new frequency to the SortedList
            freq_list.add(new_freq)
            
            # The most frequent ID count is the last element in the SortedList
            most_frequent_count = freq_list[-1] if freq_list else 0
            ans.append(most_frequent_count)
        
        return ans

def mostFrequentIDs(nums: List[int], freq: List[int]) -> List[int]:
    return Solution().mostFrequentIDs(nums, freq)