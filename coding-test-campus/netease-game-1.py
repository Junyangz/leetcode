#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
import collections
import itertools 

def sql_inner_join(a, b):
    """
    a tbname: [username]
    b username: [tbname]
    """
    del_akey = []
    del_bkey = []
    for key in b.keys():
        if len(b[key]) == 1:
            #print(b[key][0], key)
            del_bkey.append(key)
            a[b[key][0]].remove(key)
    for key in a.keys():
        if len(a[key]) <= 2:
            del_akey.append(key)
    for key in del_akey: del a[key]
    ret = []
    for username in b.keys(): 
        if username not in del_bkey:
            result = []
            for tbname in sorted(b[username]):
                if tbname in a.keys():
                    result.append(tbname)

            for t1, t2 in itertools.permutations(result, 2):
                if len(a[t1]) <= 2:
                    continue
                if (t1, t2, len(a[t1])) not in ret:
                    ret.append((t1, t2, len(a[t1])))

    for r in sorted(ret, key=lambda x: x[0]+x[1]):
        a, b, c = r
        if c > 2:
            print(a, b, c)

            # n = len(result)
            # for i in range(n - 1):
            #     for j in range(i+1, n):
            #     print(result[i], result[j], len(a[result[i]]))
            # print()

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())

    src_table = collections.defaultdict(list)
    name_table = collections.defaultdict(list)

    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        tbname, username = line.split()
        if tbname in src_table.keys():
            if username not in src_table[tbname]:
                src_table[tbname].append(username)
        else:
            src_table[tbname] = [username]
        
        #count_grater_2(src_table)

        if username in name_table.keys():
            if tbname not in name_table[username]:
                name_table[username].append(tbname)
        else:
            name_table[username] = [tbname]
        

    sql_inner_join(src_table, name_table)
        


    # print(src_table)
    # print(name_table)

# 8
# ddd Kate
# ccc Kate
# ccc Beal
# eee Tom
# ddd Beal
# bbb Kate
# ddd Tom
# ccc Tom
