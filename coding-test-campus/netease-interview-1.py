# test case pass 50%
import sys
if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())
    def check_avalible(n, m, block, tx, ty):
        if tx > n and ty > m:
            print('NO')
        for i in range(n-tx+1):
            for j in range(m-ty+1):
                for b in block:
                    if b[0] in range(i+1 , i + tx + 1) and b[1] in range(j+1, j + ty + 1):
                        break
                else:
                    print('YES')
                    return 
        print('NO')

    for i in range(n):
        n, m, k = map(int, sys.stdin.readline().strip().split())
        block = []
        for j in range(k):
            tmp = sys.stdin.readline().strip()
            block.append(list(map(int, tmp.split())))
        tx, ty = map(int, sys.stdin.readline().strip().split())

        check_avalible(n, m, block, tx, ty)

        #print('NO') if t_x > n and t_y >  m else print('YES')