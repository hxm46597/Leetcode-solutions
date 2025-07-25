class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a , b = 0 , 1
        for _ in range(n):
            a , b = b , a + b
        return a

sol = Solution()
n = 4
result = sol.fib(n)
print(result)