class Solution(object):
    def dismantlingAction(self, arr):
        """
        :type arr: str
        :rtype: int
        """
        dic, res, i = {}, 0, -1
        for j in range(len(arr)):
            if arr[j] in dic:
                i = max(dic[arr[j]], i)
            dic[arr[j]] = j
            res = max(res, j - i)
        return res
sol = Solution()
arr = "dbascDdad"
res = sol.dismantlingAction(arr)
print(res)