class Solution(object):
    def trainingPlan(self, actions):
        """
        :type actions: List[int]
        :rtype: List[int]
        """
        i, j = 0 , len(actions) - 1
        while i < j:
            while i < j and actions[i] & 1 == 1: i += 1
            while i < j and actions[j] & 1 == 0: j -= 1
            actions[i], actions[j] = actions[j], actions[i]
        return actions
actions = [1,2,3,4,5]
sol = Solution()
res = sol.trainingPlan(actions)
print(res)