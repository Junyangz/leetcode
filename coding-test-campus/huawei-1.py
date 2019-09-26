def _ban(s: str, t: str)-> str:
    r = '*' * len(t)
    return r.join(s.split(t))


if __name__ == '__main__':

    srcInput  = input().split()
    src, target = srcInput[0], srcInput[1]
    print(_ban(src, target))