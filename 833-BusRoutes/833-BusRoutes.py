# Last updated: 11/11/2025, 1:55:52 AM
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        to_routes = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i) # tracks each of i to j
        q = deque()
        q.append((source, 0))
        seen = set([source])
        while q:
            stop, bus = q.popleft()
            if stop == target:
                return bus
            for i in to_routes[stop]:
                for j in routes[i]:
                    if j not in seen:
                        q.append((j, bus+1))
                        seen.add(j)
                routes[i] = []
        return -1
        