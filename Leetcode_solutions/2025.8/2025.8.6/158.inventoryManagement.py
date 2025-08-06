class Solution(object):
    def inventoryManagement(self, stock):
        """
        :type stock: List[int]
        :rtype: int
        """
        votes = 0
        for num in stock:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x
stock = [1,2,3,2,2,2,5,4,2]
sol = Solution()
res = sol.inventoryManagement(stock)
print(res)