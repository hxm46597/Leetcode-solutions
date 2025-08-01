class Solution(object):
    def reverseMessage(self, message):
        """
        :type message: str
        :rtype: str
        """
        message = message.strip()
        strs = message.split()
        strs.reverse()
        return ' '.join(strs)
message = "a good   example"
sol = Solution()
res = sol.reverseMessage(message)
print(res)