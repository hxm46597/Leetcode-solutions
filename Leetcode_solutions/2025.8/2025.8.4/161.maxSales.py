class Solution(object):
    def maxSales(self, sales):
        """
        :type sales: List[int]
        :rtype: int
        """
        for i in range(1, len(sales)):
            sales[i] += max(sales[i - 1], 0)
        return max(sales)
sol = Solution()
sales = [-2,1,-3,4,-1,2,1,-5,4]
res = sol.maxSales(sales)
print(res)