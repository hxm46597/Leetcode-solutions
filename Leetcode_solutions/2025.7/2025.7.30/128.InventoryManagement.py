class Solution(object):
    def inventoryManagement(self, stock):
        """
        :type stock: List[int]
        :rtype: int
        """
        i, j = 0, len(stock) - 1
        while i < j:
            m = (i + j) // 2
            if stock[m] > stock[j]:
                i = m + 1
            elif stock[m] < stock[j]: j = m
            else: return min(stock[i:j])
        return stock[i]
sol = Solution()
stock = [5,7,9,1,2]
res = sol.inventoryManagement(stock)
print(res)