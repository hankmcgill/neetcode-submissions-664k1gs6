class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        current = []

        def handle_int(nums, target, start):
            # iterate through list of nums
            for i in range(start, len(nums)):
                if target == 0:
                    combinations.append(current.copy())
                    return
                
                if target < 0:
                    return
                
                current.append(nums[i])
                handle_int(nums, target - nums[i], i)
                current.pop()

        handle_int(nums, target, 0)

        return combinations