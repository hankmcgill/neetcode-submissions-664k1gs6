class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # loop through each element, for each element:
        for i in range(len(arr)):
            greatest = float('-inf')
            j = i + 1
            while j < len(arr):
                if arr[j] > greatest:
                    greatest = arr[j]
                j += 1
            # loop through all following elements, assigning current val to largest
            arr[i] = greatest
        # replace last one with -1
        arr[-1] = -1
        return arr