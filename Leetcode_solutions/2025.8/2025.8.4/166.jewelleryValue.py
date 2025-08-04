class Solution(object):
    def jewelleryValue(self, frame):
        """
        :type frame: List[List[int]]
        :rtype: int
        """
        for i in range(len(frame)):
            for j in range(len(frame[0])):
                if i == 0 and j == 0: continue
                if i == 0: frame[i][j] += frame[i][j - 1]
                elif j == 0: frame[i][j] += frame[i - 1][j]
                else: frame[i][j] += max(frame[i][j - 1], frame[i - 1][j])
        return frame[-1][-1]
sol = Solution()
frame = [[1,3,1],[1,5,1],[4,2,1]]
res = sol.jewelleryValue(frame)
print(res)