import collections

def solution(n, m, s):
    ret = n // m + 1
    for i in reversed(range(1, ret)):
        cnt = collections.Counter(s[m * i:])
        for j in range(n - m * i):
            if cnt.most_common(1)[0][1] == n - m * i:
                ret = min(ret, i)
                break
            cnt[s[j]] -= 1
            cnt[s[j + m * i]] += 1
    return ret

if __name__ == '__main__':
    n, m = input().split()
    s = str(input())
    print(solution(int(n), int(m), s))