class Solution(object):
    def crackNumber(self, ciphertext):
        """
        :type ciphertext: int
        :rtype: int
        """
        s = str(ciphertext)
        a = b = 1
        for i in range(2, len(s) + 1):
            tmp = s[i - 2: i]
            c = a + b if "10" <= tmp <= "25" else a
            b = a
            a = c
        return a
sol = Solution()
ciphertext = 216612
res = sol.crackNumber(ciphertext)
print(res)