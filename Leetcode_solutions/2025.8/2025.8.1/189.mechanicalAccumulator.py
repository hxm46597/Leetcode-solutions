class Solution(object):
    def __init__(self):
        self.res = 0

    def mechanicalAccumulator(self, target):
        """
        :type target: int
        :rtype: int
        """
        target > 1 and self.mechanicalAccumulator(target - 1)
        self.res += target
        return self.res

target = 5
sol = Solution()
result = sol.mechanicalAccumulator(target)
print(result)