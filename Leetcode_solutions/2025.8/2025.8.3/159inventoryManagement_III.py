class Solution(object):
    def inventoryManagement(self, stock, cnt):
        """
        :type stock: List[int]
        :type cnt: int
        :rtype: List[int]
        """
        def quick_sort(stock, l , r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while i < j and stock[j] >= stock[l]: j -= 1
                while i < j and stock[i] <= stock[l]: i += 1
                stock[i], stock[j] = stock[j], stock[i]
            stock[l], stock[i] = stock[i], stock[l]
            quick_sort(stock, l, i - 1)
            quick_sort(stock, i + 1, r)

        quick_sort(stock, 0, len(stock) - 1)
        return stock[:cnt]
sol = Solution()
stock = [2,5,7,4]
cnt = 1
res = sol.inventoryManagement(stock, cnt)
print(res)