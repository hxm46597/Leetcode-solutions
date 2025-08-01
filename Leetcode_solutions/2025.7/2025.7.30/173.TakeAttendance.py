class Solution(object):
    def takeAttendance(self, records):
        """
        :type records: List[int]
        :rtype: int
        """
        i , j = 0 , len(records) - 1
        while i <= j:
            m = (i + j) // 2
            if records[m] == m: i = m + 1
            else: j = m - 1
        return i
sol = Solution()
records = [0,1,2,3,5]
res = sol.takeAttendance(records)
print(res)