class Solution(object):
    def encryptionCalculate(self, dataA, dataB):
        """
        :type dataA: int
        :type dataB: int
        :rtype: int
        """
        x = 0xffffffff
        dataA, dataB = dataA & x, dataB & x
        while dataB != 0:
            dataA, dataB = (dataA ^ dataB) , (dataA & dataB) << 1 & x
        return dataA if dataA <= 0x7fffffff else ~(dataA ^ x)
sol = Solution()
dataA = 5
dataB = -1
res = sol.encryptionCalculate(dataA,dataB)
print(res)