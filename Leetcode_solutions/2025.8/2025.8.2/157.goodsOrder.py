class Solution(object):
    def goodsOrder(self, goods):
        """
        :type goods: str
        :rtype: List[str]
        """
        arr, res = list(goods), []

        def dfs(x):
            if x == len(arr) - 1:
                res.append(''.join(arr))
                return
            hmap = set()
            for i in range(x, len(arr)):
                if arr[i] in hmap: continue
                hmap.add(arr[i])
                arr[i], arr[x] = arr[x], arr[i]
                dfs(x + 1)
                arr[i], arr[x] = arr[x], arr[i]

        dfs(0)
        return res
sol = Solution()
goods = "agew"
res = sol.goodsOrder(goods)
print(res)