def solution(cmd_list: list)-> int:
    cmd, A, B = cmd_list[0], int(cmd_list[1]), int(cmd_list[2])
    if cmd == 'Q':
        print(sum(init_Sale[A-1:B]) // (B - A + 1))
    if cmd == 'U':
        init_Sale[A-1] += B
    
if __name__ == '__main__':

    first_line = input().split()
    N, M = int(first_line[0]), int(first_line[1])
    init_Sale = list(map(int, input().split()))

    for epoch in range(M):
        solution(input().split())
