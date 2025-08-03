class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 0 , 1
        for _ in range(n):
            a, b = b, (a + b) % 1000000007
        return a
n = 4
sol = Solution()
res = sol.fib(n)
print(res)