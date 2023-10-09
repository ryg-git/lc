from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from functools import cache
import heapq
from typing import *


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def findInd(lorr):
            l, r = 0, n
            while l < r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    if lorr:
                        if mid == 0 or nums[mid - 1] < target:
                            return mid
                        else:
                            r = mid
                    else:
                        if mid == n - 1 or nums[mid + 1] > target:
                            return mid
                        else:
                            l = mid + 1
                elif nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1

            return -1

        return [findInd(True), findInd(False)]


def main():
    s = Solution()
    ans = s.searchRange(nums=[2, 2], target=2)
    print(ans)


main()
