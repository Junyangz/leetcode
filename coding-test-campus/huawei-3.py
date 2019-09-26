def solution(day_stats: list)-> int:
    curr = 0
    max_point = 0
    dc= {1: 1,
        0: -1}
    cache = {}
    for i, mis in enumerate(day_stats[1:], start = 1):
        tmp = curr
        pre, s = cache.get(mis,(0,0))
        curr += sum([dc[mis > n] for n in day_stats[s:i] if mis != n]) + pre
        cache[mis] = (curr - tmp, i)
        max_point = max(curr, max_point)
    del cache
    
    print(max_point, curr)
    
if __name__ == '__main__':

    test_case = int(input())
    
    for _ in range(test_case):
        _ = int(input())
        day_stats = list(map(int, input().split()))
        solution(day_stats)
