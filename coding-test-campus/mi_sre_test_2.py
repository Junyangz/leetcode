def solution(a:list):
    a = sorted(a, key = lambda x: x[1])
    for r in a:
        print(r[0], r[1])
        
if __name__ == '__main__':
    x = int(input())
    a = []
    for i in range(x):
        a.append(list(map(int, input().split())))
    solution(a)