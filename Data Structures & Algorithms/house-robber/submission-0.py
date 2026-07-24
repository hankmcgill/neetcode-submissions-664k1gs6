class Solution:
    def rob(self, nums: List[int]) -> int:
        option1, option2 = 0, 0

        for n in nums:
            temp = max(option1 + n, option2)
            option1 = option2
            option2 = temp

        return option2