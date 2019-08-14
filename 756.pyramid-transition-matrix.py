#
# @lc app=leetcode id=756 lang=python3
#
# [756] Pyramid Transition Matrix
#
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        T = collections.defaultdict(set)
        for u, v, w in allowed:
            T[u, v].add(w)

        #Comments can be used to cache intermediate results
        #seen = set()
        def solve(A):
            if len(A) == 1: return True
            #if A in seen: return False
            #seen.add(A)
            return any(solve(cand) for cand in build(A, []))

        def build(A, ans, i = 0):
            if i + 1 == len(A):
                yield "".join(ans)
            else:
                for w in T[A[i], A[i+1]]:
                    ans.append(w)
                    for result in build(A, ans, i+1):
                        yield result
                    ans.pop()

        return solve(bottom)
#         if len(bottom) == 1: return True
#         ad = collections.defaultdict(list)
#         for x in allowed:
#             ad[x[:2]].append(x[-1])
            
#         def nextLevel(lvl):
#             if len(lvl) == 1:
#                 yield ""
#             else:
#                 for each in nextLevel(lvl[1:]):
#                     print(lvl)
#                     for brick in ad[lvl[:2]]:
#                         #print(brick, each)
#                         yield brick + each

#         def validate(lvl):
#             if len(lvl) == 1:
#                 return True

#             for each in nextLevel(lvl):
#                 print(each)
#                 if validate(each):
#                     return True

#             return False

#         return validate(bottom)
        # def genearte_next_bottom(temp = ''):
        #     for i in range(len(bottom) - 1):
        #         for v in ad[bottom[i:i+2]]:                    
        #             if len(temp) > i:
        #                 yield (temp, temp[:-1] + v)
        #             else:
        #                 temp += v
        #                 yield (temp,)
        # print(list(genearte_next_bottom()))                
        # for x in [new_bottom for new_bottom in list(
        #     genearte_next_bottom()) if len(new_bottom) == len(bottom) - 1]:
        #     print(x)
        #     return self.pyramidTransition(x, allowed)
        # return False
                    
                    
                
        
#         for i in range(len(bottom) - 1):
#             if bottom[i:i+1] in ad.keys():
                
#         return pyramidTransition() 

