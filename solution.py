from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from functools import cache, lru_cache
import heapq
from typing import *


class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (1, -2),
            (-1, -2),
            (-1, 2),
        ]

        @lru_cache(None)
        def helper(n, r, c):
            if n == 0:
                return 1
            else:
                ans = 0

                for x, y in moves:
                    nr = r + x
                    nc = c + y

                    if (0 <= nr < 3 and 0 <= nc < 3) or (nr == 3 and nc == 1):
                        ans += helper(n - 1, nr, nc)

                return ans

        ans = helper(n - 1, 3, 1)

        for i in range(3):
            for j in range(3):
                ans += helper(n - 1, i, j)

        return ans


def main():
    s = Solution()
    ans = s.knightDialer(n=2)

    print(ans)


main()
