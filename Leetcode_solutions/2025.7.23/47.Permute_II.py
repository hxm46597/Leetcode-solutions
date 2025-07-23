class Solution(object):
    def permuteUnique(self, nums):
        def dfs(x):
            if x == len(nums) - 1:
                res.append(list(nums))
                return
            dic = set()
            for i in range(x , len(nums)):
                if nums[i] in dic: continue
                dic.add(nums[i])
                nums[i] , nums[x] = nums[x] , nums[i]
                dfs(x + 1)
                nums[i] , nums[x] = nums[x] , nums[i]
        res = []
        dfs(0)
        return res
sol = Solution()
nums = [1,1,2]
result = sol.permuteUnique(nums)
print(result)