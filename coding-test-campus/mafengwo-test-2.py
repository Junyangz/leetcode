import collections
import itertools
import math


def solution(a:list, m:int):
    ret = 0
    for i in range(1, len(a)):
        retdict = {}
        mink = math.inf
        for v in itertools.permutations(a, i):
            tmp = 1
            if not v or tuple(sorted(v)) in retdict:
                continue
            for k in v:
                tmp *= k
            mink = min(tmp, mink)
            if tmp < m:
                ret += 1
                retdict[tuple(sorted(v))] = 1
        if mink > m: break   
        del retdict
        
    return ret

if __name__ == '__main__':
    a = list(map(int, (input()).split(',')))
    m = int(input())
    print(solution(a, m))