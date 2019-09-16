def isPrime(n):
    if n > 2 and n%2 == 0: 
        return 0
    i = 3 
    while i*i <= n: 
        if n % i == 0: 
            return 0
        i += 2 
    
    return 1 
if __name__ == '__main__':
    l = (input()[1:-1]).split(',')
    for n in reversed(sorted(l, key=lambda k: int(k))):
        if isPrime(int(n)): 
            print(n)
            break