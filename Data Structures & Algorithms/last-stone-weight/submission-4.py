class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            heapq.heapify_max(stones)
            stone_1 = heapq.heappop(stones)
            heapq.heapify_max(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1 == stone_2:
                continue
            elif stone_1 < stone_2:
                heapq.heappush(stones, (stone_2 - stone_1))
            else:
                heapq.heappush(stones, (stone_1 - stone_2))
        if stones:
            return stones[0]
        return 0