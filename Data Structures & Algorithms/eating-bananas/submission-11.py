class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # minimum number of hours: 
            # find smallest pile
            # for pile in piles
            # for every time that pile can be divided by smallest
                # +1 hour
            
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res