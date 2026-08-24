class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # count = float('-inf')
        count = 0

        l = 0
        r = 0

        while l < len(nums) - 1:
            if nums[l] == 1:
                temp = 1
                # start new iteration
                r = l + 1
                while r < len(nums) and nums[r] == 1:
                        temp +=1
                        r += 1
                count = max(count, temp)
            l += 1

        return count