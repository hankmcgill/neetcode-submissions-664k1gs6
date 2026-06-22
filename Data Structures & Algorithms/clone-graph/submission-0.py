"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}
        
        queue = deque()
        queue.append(node)

        # traverse entire graph using bfs
        while queue:
            for _ in range(len(queue)):
                # add node to object
                curr = queue.popleft()
                curr_val = curr.val

                # end of one level

        return cloned