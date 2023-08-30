from bisect import bisect_left, bisect_right
from collections import deque
from typing import *

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        l = len(nums) - 1
        
        las = nums[l]

        ans = 0

        for i in range(l - 1, -1, -1):
            if nums[i] > las:
                t = nums[i] // las
                if nums[i] % las:
                    t += 1
                las = nums[i] // t
                ans = t - 1
            else:
                las = nums[i]

        return ans


def main():
    s = Solution()
    ans = s.minimumReplacement(nums=[3, 9, 3])
    print(ans)


main()
