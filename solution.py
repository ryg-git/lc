from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
import heapq
from typing import *


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:

        def find_max(arr: List[int]):
            st = [(arr[0], arr[0])]
            n = len(arr)

            for i in range(1, n):
                cnt = 1
                j = i
                while j > 0 and arr[j - 1] > arr[j]:
                    s, c = st[j]
                    cnt += c
                    j -= 1

                if st:
                    su += st[-1][1]

                st.append((h, su + cnt * h, cnt))

            return st

        le = [0] + list(map(lambda x: x[1], find_max(maxHeights)))

        return le


def main():
    s = Solution()
    ans = s.maximumSumOfHeights(maxHeights=[3, 2, 5, 5, 2, 3])
    print(ans)


main()
