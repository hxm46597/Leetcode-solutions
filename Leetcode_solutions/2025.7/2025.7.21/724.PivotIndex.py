class Solution(object):
    def pivotIndex(self, nums):
        sum_left, sum_right = 0, sum(nums)
        for i in range(len(nums)):
            sum_right -= nums[i]
            if sum_left == sum_right:
                return i
            sum_left += nums[i]
        return -1
sol = Solution()
nums = [1,7,3,6,5,6]
result = sol.pivotIndex(nums)
print(result)