from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a < b:
                return 1
            elif a > b:
                return -1
            else:
                return 0

        strs = [str(num) for num in nums]
        strs.sort(key=cmp_to_key(sort_rule))
        if strs[0] == "0":
            return "0"
        return ''.join(strs)
nums = [3,30,34,5,9]
sol = Solution()
result = sol.largestNumber(nums)
print(result)