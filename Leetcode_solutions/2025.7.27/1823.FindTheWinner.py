class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        x = 0
        for i in range(2, n + 1):
            x = (x + k) % i
        return x + 1
sol = Solution()
n = 5
k = 2
res = sol.findTheWinner(n,k)
print(res)