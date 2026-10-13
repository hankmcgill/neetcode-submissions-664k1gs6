class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if self.searchRow(row, target) is True:
                return True
        return False

    def searchRow(self, row: List[int], target: int) -> True:
        l, r = 0, len(row) - 1

        if r <= 1:
            return self.searchLR(row[l], row[r], target)

        while (l + 1) < r:
            mid = math.floor((l + r) / 2)
            if row[mid] == target or self.searchLR(row[l], row[r], target) is True:
                return True
            elif row[mid] < target:
                l = mid
            else:
                r = mid
        
        return False

    def searchLR(self, l: int, r: int, target: int):
        if l == target or r == target:
            return True
        return False
