class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i)
            dic[s[j]] = j
            res = max(res, j - i)
        return res
sol = Solution()
s = "pwwkew"
result = sol.lengthOfLongestSubstring(s)
print(result)