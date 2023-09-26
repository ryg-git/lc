'''input

'''
import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd, deque
from bisect import bisect_left as bl, bisect_right as br

sys.setrecursionlimit(100000000)


def inp(): return int(input())
def strng(): return input().strip()


def jn(x, l): return x.join(map(str, l))
def strl(): return list(input().strip())


def mul(): return map(int, input().strip().split())
def mulf(): return map(float, input().strip().split())
def seq(): return list(map(int, input().strip().split()))


def ceil(x): return int(x) if (x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if (x % d == 0) else x//d+1


def flush(): return stdout.flush()
def stdstr(): return stdin.readline()
def stdint(): return int(stdin.readline())


def stdpr(x): return stdout.write(str(x))


mod = 1000000007

# main code


def solution():
    k = inp()

    if k < 10:
        return k
    else:
        k -= 9
        
        q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
        
        while q:
            nu = q.popleft()
            
            ln = nu % 10
            
            for i in range(ln):
                q.append(nu * 10 + i)
                k -= 1
                if k == 0:
                    num = q.pop()
                    return num
        return -1


def main():
    t = 1

    for _ in range(t):
        ans = solution()
        print(ans)


main()
