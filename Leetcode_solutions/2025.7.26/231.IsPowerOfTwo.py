class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n & (n - 1) == 0
n1 = 128
n2 = 3
sol = Solution()
res1 = sol.isPowerOfTwo(n1)
res2 = sol.isPowerOfTwo(n2)
print(res1,res2)