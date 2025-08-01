class Solution(object):
    def countTarget(self, scores, target):
        """
        :type scores: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, len(scores) - 1
        while i <= j:
            m = (i + j) // 2
            if scores[m] <= target: i = m + 1
            else: j = m - 1
        right = i
        if j >= 0 and scores[j] != target: return 0
        i = 0
        while i<= j:
            m = (i + j) // 2
            if scores[m] < target: i = m + 1
            else: j = m - 1
        left = j
        return right - left - 1

sol = Solution()
scores = [2,2,3,4,4,4,5,6,6,8]
target = 4
res = sol.countTarget(scores, target)
print(res)