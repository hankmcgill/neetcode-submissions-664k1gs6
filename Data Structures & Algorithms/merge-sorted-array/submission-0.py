class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = 0
        j = 0

        if m == 0:
            if nums2:
                for val in nums2:
                    nums1.pop(0)
                    nums1.append(val)
            return nums1

        while nums2 and i < len(nums1) and n:
            if nums1[i] >= nums2[j]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                nums2.pop(0)
                n -= 1
            i += 1

        if nums2:
            for val in nums2:
                nums1.append(val)
        return nums1