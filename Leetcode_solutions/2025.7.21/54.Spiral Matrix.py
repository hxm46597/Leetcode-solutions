class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix : return []
        l,r,t,b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = []
        while True:
            for i in range(l, r + 1):res.append(matrix[t][i])#left yo right
            t += 1
            if t > b:break
            for i in range(t, b + 1):res.append(matrix[i][r])#top to bottom
            r -= 1
            if l > r:break
            for i in range(r, l - 1, -1):res.append(matrix[b][i])#right to left
            b -= 1
            if t > b:break
            for i in range(b, t - 1, -1):res.append(matrix[i][l])#bottom to top
            l += 1
            if l > r:break
        return res
sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = sol.spiralOrder(matrix)
print(result)