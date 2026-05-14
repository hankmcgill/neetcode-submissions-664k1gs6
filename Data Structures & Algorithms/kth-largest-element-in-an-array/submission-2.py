class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        val = None
        for i in range(k):
            heapq.heapify_max(nums)
            val = heapq.heappop(nums)
        return val