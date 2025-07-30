class Solution(object):
    def dismantlingAction(self, arr):
        """
        :type arr: str
        :rtype: str
        """
        hmap = {}
        for c in arr:
            hmap[c] = not c in hmap
        for c in arr:
            if hmap[c]: return c
        return ' '
sol = Solution()
arr = "abbccdeff"
res = sol.dismantlingAction(arr)
print(res)