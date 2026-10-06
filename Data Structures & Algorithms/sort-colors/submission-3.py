class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]

        for i in nums:
            counts[i] += 1

        idx = 0
        for i in range(3):
            for j in range(counts[i]):
                nums[idx] = i
                idx += 1

        return nums