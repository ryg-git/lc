from bisect import bisect_left, bisect_right
from collections import deque
from typing import *


class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        dp = [1] * (l)

        for i in range(1, l):
            if ratings[i] > ratings[i - 1] and dp[i] <= dp[i - 1]:
                dp[i] = dp[i - 1] + 1

        for i in range(l - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and dp[i] <= dp[i - 1]:
                dp[i] = dp[i + 1] + 1

        return sum(dp)


def main():
    s = Solution()
    ans = s.candy(ratings=[1, 3, 2, 2, 1])
    print(ans)


main()
