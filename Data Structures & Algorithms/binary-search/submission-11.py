class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        if r == 1 and nums[r - 1] == target:
            return r - 1

        while (l + 1) < r:
            if nums[r - 1] == target:
                return r - 1
            if nums[l] == target:
                return l
            mid = int(math.floor(l + r) / 2)
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                r = mid
            else:
                l = mid

        return -1