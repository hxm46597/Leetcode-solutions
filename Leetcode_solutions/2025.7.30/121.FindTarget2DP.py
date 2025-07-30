class Solution(object):
    def findTargetIn2DPlants(self, plants, target):
        """
        :type plants: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i , j = len(plants) - 1, 0
        while i >= 0 and j < len(plants[0]):
            if plants[i][j] > target: i -= 1
            elif plants[i][j] < target: j += 1
            else: return True
        return False
plants = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
sol = Solution()
res = sol.findTargetIn2DPlants(plants, target)
print(res)