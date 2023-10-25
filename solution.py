from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from functools import cache
import heapq
from typing import *


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        def rec(nn: int, kk: int):
            if nn == 1:
                return 0

            mid = nn // 2

            if mid >= kk:
                return rec(mid, kk)
            else:
                return 1 - rec(mid, kk - mid)

        return rec(nn=2 ** (n - 1), kk=k)


def main():
    s = Solution()
    ans = s.kthGrammar(n=2, k=2)
    print(ans)


main()
