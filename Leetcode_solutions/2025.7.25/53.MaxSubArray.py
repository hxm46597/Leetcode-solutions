class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)

nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
result = sol.maxSubArray(nums)
print(result)