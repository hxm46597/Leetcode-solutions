class Solution(object):
    def statisticalResult(self, arrayA):
        """
        :type arrayA: List[int]
        :rtype: List[int]
        """
        arrayB , tmp = [1] * len(arrayA), 1
        for i in range(1, len(arrayA)):
            arrayB[i] = arrayB[i - 1] * arrayA[i - 1]
        for i in range(len(arrayA) - 2, -1 , -1):
            tmp *= arrayA[i + 1]
            arrayB[i] *= tmp
        return arrayB
sol = Solution()
arrayA = [2,4,6,8,10]
res = sol.statisticalResult(arrayA)
print(res)