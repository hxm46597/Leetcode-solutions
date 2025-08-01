class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans, tmp = [1] * len(nums), 1
        for i in range(1, len(nums)):
            ans [i] = ans[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            tmp *= nums[i + 1]
            ans[i] *= tmp
        return ans
sol = Solution()
nums = [1,2,3,4]
result = sol.productExceptSelf(nums)
print(result)