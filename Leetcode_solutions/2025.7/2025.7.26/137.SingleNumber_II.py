class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0 , 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
sol = Solution()
nums = [0,1,0,1,0,1,99]
result= sol.singleNumber(nums)
print(result)