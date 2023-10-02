from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
import heapq
from typing import *


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        sn = sum(nums)
        n = len(nums)

        d = target // sn
        r = target % sn

        def find_len(nu, tar, mm):

            ml = 100001 if mm else -1

            def check(nu, a):
                return min(nu, a) if mm else max(nu, a)

            su, r, l = 0, 0, 0

            while l <= r and l < n:
                if su == tar:
                    ml = check(ml, r - l)
                if r < n and su < tar:
                    su += nu[r]
                    r += 1
                else:
                    su -= nu[l]
                    l += 1

            return ml

        o = find_len(nums, r, True)
        t = find_len(nums, sn - r, False)

        if o == 100001 and t == -1:
            return -1
        elif o == 100001:
            return d * n + (n - t)
        elif t == -1:
            return d * n + o
        else:
            return d * n + min(o, n - t)


def main():
    s = Solution()
    ans = s.minSizeSubarray(
        nums=[1, 4, 8, 5, 9, 8, 8, 2, 3, 1, 6, 2, 7, 5, 5, 3, 3, 5, 6], target=57)
    print(ans)


main()
