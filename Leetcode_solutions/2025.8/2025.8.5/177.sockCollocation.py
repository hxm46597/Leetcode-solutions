class Solution(object):
    def sockCollocation(self, sockets):
        """
        :type sockets: List[int]
        :rtype: List[int]
        """
        x, y, n, m = 0, 0, 0, 1
        for num in sockets:
            n ^= num
        while n & m == 0:
            m <<= 1
        for num in sockets:
            if num & m: x ^= num
            else: y ^= num
        return [x, y]
sockets = [1,2,4,1,4,3,12,3]
sol = Solution()
res = sol.sockCollocation(sockets)
print(res)