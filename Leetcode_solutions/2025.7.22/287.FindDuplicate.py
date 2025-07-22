class Solution(object):
    def findDuplicate(self, nums):
        a = set()
        for num in nums:
            if num in a:
                return num
            a.add(num)
        return -1
sol = Solution()
nums = [1,3,4,2,2]
result = sol.findDuplicate(nums)
print(result)