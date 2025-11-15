import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def custom_sort(log):
            # Split the log into identifier and content
            identifier, content = log.split(' ', 1)
            # Check if the log is a letter-log
            if content[0].isalpha():
                # Return a tuple that will sort letter-logs by content then identifier
                return (0, content, identifier)
            else:
                # Return a tuple that will place digit-logs after letter-logs
                return (1,)

        # Sort the logs using the custom sort function
        logs.sort(key=custom_sort)
        return logs

def reorderLogFiles(logs: List[str]) -> List[str]:
    return Solution().reorderLogFiles(logs)