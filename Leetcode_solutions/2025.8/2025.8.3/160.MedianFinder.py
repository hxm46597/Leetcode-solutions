from heapq import *

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []
        self.B = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.A) != len(self.B):
            heappush(self.B, -heappushpop(self.A, num))
        else:
            heappush(self.A, -heappushpop(self.B, -num))

    def findMedian(self):
        """
        :rtype: float
        """
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
print(obj.addNum(1))
print(obj.addNum(2))
print(obj.findMedian())
print(obj.addNum(3))
print(obj.findMedian())