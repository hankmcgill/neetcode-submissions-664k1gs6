class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        n_1, n_2 = (n - 1), (n - 2)

        l = self.climbStairs(n_1)
        r = self.climbStairs(n_2)

        return l + r