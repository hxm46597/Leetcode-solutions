class Solution(object):
    def trainingPlan(self, actions):
        """
        :type actions: List[int]
        :rtype: int
        """
        ones , twos = 0, 0
        for action in actions:
            ones = ones ^ action & ~twos
            twos = twos ^ action & ~ones
        return ones

sol = Solution()
actions = [12,1,6,12,6,12,6]
res = sol.trainingPlan(actions)
print(res)