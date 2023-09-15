from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
import heapq
from typing import *


def manhattan_distance(p1: List[int], p2: List[int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, u):
        if self.parent[u] == u:
            return u
        else:
            self.parent[u] = self.find(self.parent[u])
            return self.parent[u]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return False
        else:
            if self.rank[u] < self.rank[v]:
                u, v = v, u

            self.parent[v] = u

            if self.rank[v] == self.rank[u]:
                self.rank[u] += 1


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        uf = UnionFind(n)

        hp = []

        for i in range(n):
            for j in range(i + 1, n):
                d = manhattan_distance(points[i], points[j])
                
                heapq.heappush((d, i, j))

        mst_wt = 0
        mst_ed = 0

        while hp:
            w, u, v = heapq.heappop(hp)
            
            if uf.union(u, v):
                mst_wt += w
                mst_ed += 1
                
                if mst_ed - 1 == n:
                    break

        return mst_wt


def main():
    s = Solution()
    ans = s.minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]])
    print(ans)


main()
