class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num: i = m + 1
                else:j = m
            tails[i] = num
            if j == res: res += 1
        return res

sol = Solution()
nums = [10,9,2,5,3,7,101,18]
result = sol.lengthOfLIS(nums)
print(result)