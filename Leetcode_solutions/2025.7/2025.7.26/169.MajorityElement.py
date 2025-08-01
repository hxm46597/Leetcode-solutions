class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x
sol = Solution()
nums = [2,2,1,1,1,2,2]
result = sol.majorityElement(nums)
print(result)