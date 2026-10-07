class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        idx = -1

        while (l + 1) < r:
            mid = int(math.floor(l + r) / 2)
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                r = mid
            else:
                l = mid

        return idx