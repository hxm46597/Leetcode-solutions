def isBadVersion(version):
    # 这里的 bad 是测试数据中的错误版本号，需要在测试时设置
    return version >= bad
class Solution(object):
    def firstBadVersion(self, n):
        i , j = 1 , n
        while i <= j:
            m = i + (j - i) // 2
            if isBadVersion(m) : j = m - 1
            else:i = m + 1
        return i


if __name__ == "__main__":
    n = 5  # 总版本数
    bad = 4  # 第一个错误的版本

    solution = Solution()
    result = solution.firstBadVersion(n)
    print(int(result))