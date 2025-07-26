class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res
sol = Solution()
n = 2147483645
result = sol.hammingWeight(n)
print(result)