class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = [0] * len(nums)
        sum[0] = nums[0]
        for i in range(1, len(nums)):
            sum[i] = nums[i] + sum[i - 1]
        return sum

nums = [3,1,2,10,1]
sol = Solution()
result = sol.runningSum(nums)
print(result)