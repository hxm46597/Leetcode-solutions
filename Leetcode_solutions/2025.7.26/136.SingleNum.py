class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for num in nums:
            x ^= num
        return x
nums = [4,1,2,1,2]
sol = Solution()
result = sol.singleNumber(nums)
print(result)