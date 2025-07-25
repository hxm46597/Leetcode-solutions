class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur , pre = max(pre + num, cur) , cur
            return cur
        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]
nums = [2 , 23, 9 , 3 , 20]
sol = Solution()
result = sol.rob(nums)
print(result)