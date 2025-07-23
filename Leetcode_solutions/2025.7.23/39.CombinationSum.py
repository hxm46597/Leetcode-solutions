class Solution(object):
    def combinationSum(self, candidates, target):
        def backtrack(
                state: list[int], target: int, choices: list[int], start: int, res: list[list[int]]
        ):
            if target == 0:
                res.append(list(state))
                return
            for i in range(start, len(choices)):
                if target - choices[i] < 0:
                    break
                state.append(choices[i])
                backtrack(state, target - choices[i], choices, i, res)
                state.pop()

        state = []
        candidates.sort()
        start = 0
        res = []
        backtrack(state, target, candidates, start, res)
        return res

sol = Solution()
candidates = [2,3,6,7]
target = 7
result = sol.combinationSum(candidates,target)
print(result)