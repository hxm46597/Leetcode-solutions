class Solution(object):
    def permute(self, nums):
        def dfs(x):
            if x == len(nums) - 1:
                res.append(list(nums))
                return
            for i in range(x,len(nums)):
                nums[i] , nums[x] = nums[x] , nums[i]
                dfs(x + 1)
                nums[i] , nums[x] = nums[x] , nums[i]
        res = []
        dfs(0)
        return res
sol = Solution()
nums = [1,2,3]
result = sol.permute(nums)
print(result)