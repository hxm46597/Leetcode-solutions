class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s : return 0
        res , i ,sign = 0 , 1, 1
        int_max  , int_min , bndry = 2**31 - 1, -2 ** 31, 2 ** 31 // 10
        if s[0] == '-': sign = -1
        elif s[0] != '+' : i = 0
        for c in s[i:]:
            if not '0' <= c <= '9':break
            if res > bndry or res == bndry and c > '7': return int_max if sign == 1 else int_min
            res = 10 * res + ord(c) - ord('0')
        return sign * res
sol = Solution()
s1 = '+1234'
s2 = '-123'
s3 = '123'
s4 = '123abc'
s5 = '123  45'
s6 = 'abc123'
print(sol.myAtoi(s1))
print(sol.myAtoi(s2))
print(sol.myAtoi(s3))
print(sol.myAtoi(s4))
print(sol.myAtoi(s5))
print(sol.myAtoi(s6))