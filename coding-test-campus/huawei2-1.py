def solution(s: str, target: str)-> int:
    s = "".join(s.split())

    start = numTarget = 0 
    while start >= 0:
        pos = s.find(target, start)
        if pos < 0:
            break
        numTarget += 1
        start = pos + 1
    return numTarget


if __name__ == '__main__':

    srcInput = input()
    target = input()
    
    print(solution(srcInput, target))