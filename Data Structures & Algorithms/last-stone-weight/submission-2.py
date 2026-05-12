class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create a heap, only values that matter are the top two values
        # iteratively pop the lesser of the two or both if equal weight
        # when there's 1 left:
            # return weight
        # return 0

        heapq.heapify_max(stones)
        print(stones)

        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            heapq.heapify_max(stones)
            stone_2 = heapq.heappop(stones)
            print("stone_1, stone_2")
            print(stone_1, stone_2)
            if stone_1 == stone_2:
                continue
            elif stone_1 < stone_2:
                heapq.heappush(stones, (stone_2 - stone_1))
            else:
                heapq.heappush(stones, (stone_1 - stone_2))
        
        if stones:
            return stones[0]
        return 0