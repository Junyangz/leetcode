class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start <= destination: s, d = start, destination
        else: d, s = start, destination
        return min(sum(distance[s:d]), sum(distance[:s]) + sum(distance[d:]))