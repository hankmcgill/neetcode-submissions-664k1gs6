class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(start):
            # add current subset (copy!)
            result.append(subset[:])

            for i in range(start, len(nums)):
                # include nums[i]
                subset.append(nums[i])
                
                # recurse
                backtrack(i + 1)
                
                # backtrack (remove last element)
                subset.pop()

        backtrack(0)
        return result