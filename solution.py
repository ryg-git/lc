from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from functools import cache
import heapq
from typing import *


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            prev = [1, 1]

            for _ in range(1, rowIndex):
                nr = [0] * (len(prev) + 1)

                nr[0], nr[-1] = 1, 1

                for j in range(1, len(prev)):
                    nr[j] = prev[j - 1] + prev[j]
                
                prev = nr[:]

            return prev


def main():
    s = Solution()
    ans = s.getRow(rowIndex=3)
    print(ans)


main()
