class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a , b = 1 , 1
        for _ in range(n):
            a , b = b , a + b
        return a
sol = Solution()
n = 4
result = sol.climbStairs(n)
print(result)