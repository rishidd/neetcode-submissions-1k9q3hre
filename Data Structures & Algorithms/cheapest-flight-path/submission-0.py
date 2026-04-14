class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u,v,w in flights:
            adj[u].append((v,w))

        min_cost = [float('inf')] * n
        min_cost[src] = 0
        queue = collections.deque([(0,src,0)]) #stops, node, cost

        while queue:
            stops, node, cost = queue.popleft()
            if stops > k:
                continue
            for v,w in adj[node]:
                next_cost = cost + w
                if next_cost < min_cost[v]:
                    min_cost[v] = next_cost
                    queue.append((stops + 1, v, next_cost))
        
        return min_cost[dst] if min_cost[dst] != float('inf') else -1