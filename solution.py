from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
import heapq
from typing import *


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        a = sorted(tickets, reverse=True)

        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        itinerary = []

        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            itinerary.append(airport)

        dfs("JFK")

        return itinerary[::-1]


def main():
    s = Solution()
    ans = s.findItinerary(
        tickets=[["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])
    print(ans)


main()
