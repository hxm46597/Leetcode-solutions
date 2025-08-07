class Solution(object):
    def findKthNumber(self, k):
        """
        :type k: int
        :rtype: int
        """
        digit, start, count = 1, 1, 9
        while k > count:
            k -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (k - 1) // digit
        return int(str(num)[(k - 1) % digit])
sol = Solution()
num = 12
res = sol.findKthNumber(num)
print(res)