class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur , pre = 0 , 0
        for num in nums:
            cur, pre = max(pre + num , cur), cur
        return cur
nums = [2 , 23, 9 , 3 , 20]
sol = Solution()
result = sol.rob(nums)
print(result)