import copy
class Solution(object):
    def rotate(self, matrix):
         n = len(matrix)
         for i in range(n // 2):
            for j in range((n + 1) // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n- 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = tmp
            return matrix
sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
result = sol.rotate(matrix)
print(result)