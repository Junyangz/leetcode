# started with wrong understanding, so can not solve it.
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        result = []
        by_name = collections.defaultdict(dict)
        for t in transactions:
            name, tt, _, city = t.split(',')
            time = int(tt)

            if city not in by_name[name]:
                by_name[name][city] = []
            by_name[name][city].append(time)
        
        for t in transactions:
            name, tt, a, city = t.split(',')
            time = int(tt)
            amount = int(a)
            if amount > 1000:
                result.append(t)
            else:
                should_add = False
                for c in by_name[name]:
                    if c != city:
                        for tc in by_name[name][c]:
                            if abs(tc-time) <= 60:
                                should_add = True
                                break
                if should_add:
                    result.append(t)
        return result

#         Td = collections.defaultdict(list)
#         for t in T:
#             name = t.split(',')[0]
#             if name in Td.keys():
#                 Td[name].append(t.split(',')[1:])
#             else:
#                 Td[name] = [t.split(',')[1:]]

#         ret = []
#         for name in Td.keys():
#             if len(Td[name]) > 1:
#                 temp = sorted(Td[name],key = lambda t: int(t[0]))
#                 for i in range(1, len(temp)):
#                     if int(temp[i][0]) - int(temp[i-1][0]) <= 60 and temp[i-1][-1] != temp[i][-1]:
#                         if ','.join([name]+temp[i]) not in ret:
#                             ret.append(','.join([name]+temp[i]))
#                         if ','.join([name]+temp[i-1]) not in ret:
#                             ret.append(','.join([name]+temp[i-1]))
#                 for t in Td[name]:
#                     if int(t[1]) > 1000: 
#                         if ','.join([name]+t) not in ret:
#                             ret.append(','.join([name]+t))
#             else:
#                 if int(Td[name][0][1]) > 1000:
#                     ret.append(','.join([name]+Td[name][0]))
#         return ret
