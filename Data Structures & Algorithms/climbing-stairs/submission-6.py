class Solution:
    cache = {}
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        n_1, n_2 = (n - 1), (n - 2)

        if n_1 in self.cache.keys():
            l = self.cache[n_1]
        else:
            self.cache[n_1] = self.climbStairs(n_1)
            l = self.climbStairs(n_1)

        if n_2 in self.cache.keys():
            r = self.cache[n_2]
        else:
            self.cache[n_2] = self.climbStairs(n_2)
            r = self.climbStairs(n_2)

        return l + r