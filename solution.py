from bisect import bisect_left, bisect_right
from typing import *


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort(key=lambda p: p[1])

        last = float('-inf')

        ans = 0

        for a, b in pairs:
            if last < a:
                last = b
                ans += 1

        return ans


def main():
    s = Solution()
    ans = s.findLongestChain(pairs=[[1, 2], [2, 3], [3, 4]])
    print(ans)


main()
