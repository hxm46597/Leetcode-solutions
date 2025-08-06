import math
class Solution(object):
    def cuttingBamboo(self, bamboo_len):
        """
        :type bamboo_len: int
        :rtype: int
        """
        if  bamboo_len <= 3: return bamboo_len - 1
        a, b = bamboo_len // 3, bamboo_len % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)
sol = Solution()
bamboo_len = 12
res = sol.cuttingBamboo(bamboo_len)
print(res)