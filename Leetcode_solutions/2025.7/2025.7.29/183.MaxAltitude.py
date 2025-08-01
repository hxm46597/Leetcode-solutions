import collections
class Solution(object):
    def maxAltitude(self, heights, limit):
        """
        :type heights: List[int]
        :type limit: int
        :rtype: List[int]
        """
        if not heights or limit == 0: return []
        deque = collections.deque()
        for i in range(limit):
            while deque and deque[-1] < heights[i]:
                deque.pop()
            deque.append(heights[i])
        res = [deque[0]]

        for i in range(limit, len(heights)):
            if deque[0] == heights[i - limit]:
                deque.popleft()
            while deque and deque[-1] < heights[i]:
                deque.pop()
            deque.append(heights[i])
            res.append(deque[0])
        return res
heights = [14,2,27,-5,28,13,39]
limit = 3
sol = Solution()
res = sol.maxAltitude(heights, limit)
print(res)