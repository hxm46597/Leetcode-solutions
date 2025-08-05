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
n = 0o0000000000000000000000000000011
sol = Solution()
res = sol.hammingWeight(n)
print(res)