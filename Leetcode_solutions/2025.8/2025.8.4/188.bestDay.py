class Solution(object):
    def bestTiming(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cost , profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit
prices = [3,6,2,9,8,5]
sol = Solution()
res = sol.bestTiming(prices)
print(res)