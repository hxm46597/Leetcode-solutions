class Solution(object):
    def twoSum(self, price, target):
        """
        :type price: List[int]
        :type target: int
        :rtype: List[int]
        """
        i , j = 0 , len(price) - 1
        while i < j:
            s = price[i] + price[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return price[i], price[j]
        return []