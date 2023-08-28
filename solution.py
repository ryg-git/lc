from bisect import bisect_left, bisect_right
from collections import deque
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return None

def main():
    s = Solution()
    ans = s.canCross(stones=[0, 1, 3, 5, 6, 8, 12, 17])
    print(ans)

main()
