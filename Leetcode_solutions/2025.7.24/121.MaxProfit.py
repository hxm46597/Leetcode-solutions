class Solution(object):
    def maxProfit(self, prices):
        cost , profit = float('+inf'), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit
sol = Solution()
prices = [7,1,5,3,6,4]
result = sol.maxProfit(prices)
print(result)