class Solution(object):
    def search(self, nums, target):
        i , j = 0 , len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            elif nums[m] > target:
                j = m - 1
            else:
                return m
        return -1
sol = Solution()
nums1 = [-1,0,3,5,9,12]
target1 = 9
nums2 = [-1,0,3,5,9,12]
target2 = 2
print(sol.search(nums1,target1))
print(sol.search(nums2,target2))