class Solution(object):
    def convert(self, s, numRows):
        if numRows < 2: return s
        res = [""for _ in range(numRows)]
        i , flag = 0,-1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:flag = - flag
            i += flag
        return "".join(res)
if __name__ == "__main__":
    sol = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    result = sol.convert(s,numRows)
    print(result)