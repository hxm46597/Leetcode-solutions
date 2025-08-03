class Solution(object):
    def checkDynasty(self, places):
        """
        :type places: List[int]
        :rtype: bool
        """
        repeat = set()
        ma, mi = 0, 14
        for place in places:
            if place == 0: continue
            ma = max(ma, place)
            mi = min(mi, place)
            if place in repeat: return False
            repeat.add(place)
        return ma - mi < 5

places = [0,6,9,0,7]
sol = Solution()
res = sol.checkDynasty(places)
print(res)