class Solution(object):
    def findKthLargest(self, nums, k):
        return sorted(nums)[len(nums) - k]
sol = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
result = sol.findKthLargest(nums,k)
print(result)