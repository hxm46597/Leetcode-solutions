class Solution(object):
    def trainWays(self, num):
        """
        :type num: int
        :rtype: int
        """
        a , b = 1 , 1
        for _ in range(num):
            a , b = b , (a + b) % 1000000007
        return a
sol = Solution()
num = 5
res = sol.trainWays(num)
print(res)