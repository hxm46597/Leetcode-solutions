class Solution(object):
    def combinationSum2(self, candidates, target):
        def backtrack(
                state: list[int], target: int, choices: list[int], start: int, res: list[list[int]]
        ):
            if target == 0:
                res.append(list(state))
                return
            for i in range(start, len(choices)):
                if target - choices[i] < 0:
                    break

                if i > start and choices[i] == choices[i - 1]:
                    continue

                state.append(choices[i])

                backtrack(state, target - choices[i], choices, i + 1, res)
                state.pop()

        state = []
        candidates.sort()
        start = 0
        res = []
        backtrack(state, target, candidates, start, res)
        return res

sol = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
result = sol.combinationSum2(candidates,target)
print(result)