class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        oldmax = -1

        for i in range(len(arr) - 1, -1, -1):
            curr_max = max(oldmax, arr[i])
            arr[i] = oldmax
            oldmax = curr_max
        
        return arr