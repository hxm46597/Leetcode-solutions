class Solution(object):
    def cuttingBamboo(self, bamboo_len):
        """
        :type bamboo_len: int
        :rtype: int
        """
        if  bamboo_len <= 3: return bamboo_len - 1
        a, b, p, x, rem = bamboo_len // 3 - 1, bamboo_len % 3, 1000000007, 3, 1
        while a > 0:
            if a % 2: rem = (rem * x) % p
            x = x ** 2 % p
            a //= 2
        if b == 0: return (rem * 3) % p
        if b == 1: return (rem * 4) % p
        return (rem * 6) % p
sol = Solution()
bamboo = 120
res = sol.cuttingBamboo(bamboo)
print(res)