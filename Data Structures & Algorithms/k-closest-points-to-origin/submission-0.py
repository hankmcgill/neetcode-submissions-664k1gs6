import math
import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for point in points:
            x_sq = point[0] ** 2
            y_sq = point[1] ** 2
            dist = math.sqrt(x_sq + y_sq)

            distances.append((dist, point))

        heapq.heapify(distances)

        result = []

        for _ in range(k):
            result.append(heapq.heappop(distances)[1])

        return result