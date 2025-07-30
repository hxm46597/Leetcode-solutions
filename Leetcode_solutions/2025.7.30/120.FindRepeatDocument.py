class Solution(object):
    def findRepeatDocument(self, documents):
        """
        :type documents: List[int]
        :rtype: int
        """
        i = 0
        while i < len(documents):
            if documents[i] == i:
                i += 1
                continue
            if documents[documents[i]] == documents[i]: return documents[i]
            documents[documents[i]], documents[i] = documents[i], documents[documents[i]]
        return -1
documents = [2, 5, 3, 0, 5, 0]
sol = Solution()
res = sol.findRepeatDocument(documents)
print(res)