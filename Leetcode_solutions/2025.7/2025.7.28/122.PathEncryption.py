class Solution(object):
    def pathEncryption(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = []
        for i in path:
            if i == '.':
                res.append(' ')
            else:
                res.append(i)
        return "".join(res)
sol = Solution()
path = "a.aef.qerf.bb"
res = sol.pathEncryption(path)
print(res)