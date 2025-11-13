

import heapq
class Logger(object):
    

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heap = []
        self.cache = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        while len(self.heap):
            if self.heap[0][0] <= timestamp:
                temp = heapq.heappop(self.heap)
                self.cache.pop(temp[1])
            else:
                break
        if timestamp < self.cache.get(message, 0):
            return False
        self.cache[message] = timestamp + 10
        heapq.heappush(self.heap, (timestamp + 10, message))
        return True