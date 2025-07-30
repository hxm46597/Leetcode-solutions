class Solution(object):
    def spiralArray(self, array):
        """
        :type array: List[List[int]]
        :rtype: List[int]
        """
        if not array: return []
        l, r, t, b = 0, len(array[0]) - 1, 0, len(array) - 1
        res = []
        while True:
            for i in range(l, r + 1): res.append(array[t][i])
            t += 1
            if t > b: break
            for i in range(t, b + 1): res.append(array[i][r])
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1): res.append(array[b][i])
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1): res.append(array[i][l])
            l += 1
            if l > r: break
        return res
array = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
sol = Solution()
res = sol.spiralArray(array)
print(res)