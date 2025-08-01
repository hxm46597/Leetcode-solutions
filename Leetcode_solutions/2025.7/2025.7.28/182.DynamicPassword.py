class Solution(object):
    def dynamicPassword(self, password, target):
        """
        :type password: str
        :type target: int
        :rtype: str
        """
        res = []
        tmp = password[0: target]
        tmp2 = password[target: ]
        res.append(tmp2)
        res.append(tmp)
        return "".join(res)
password = "s3cur1tyC0d3"
target = 4
sol = Solution()
res = sol.dynamicPassword(password,target)
print(res)