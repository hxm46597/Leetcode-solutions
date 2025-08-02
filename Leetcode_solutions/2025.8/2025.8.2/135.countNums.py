class Solution(object):
    def countNumbers(self, cnt):
        """
        :type cnt: int
        :rtype: List[int]
        """
        def dfs(x):
            if x == cnt:
                s = ''.join(num[self.start:])
                if s != '0': res.append(int(s))
                if cnt - self.start == self.nine: self.start -= 1
                return
            for i in range(10):
                if i == 9: self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1

        num, res = ['0'] * cnt, []
        self.nine = 0
        self.start = cnt - 1
        dfs(0)
        return res
sol = Solution()
cnt = 2
res = sol.countNumbers(cnt)
print(res)