class Solution(object):
    def iceBreakingGame(self, num, target):
        """
        :type num: int
        :type target: int
        :rtype: int
        """
        x = 0
        for i in range(2, num + 1):
            x = (x + target) % i
        return x
sol = Solution()
num = 7
target = 4
res = sol.iceBreakingGame(num, target)
print(res)