class Solution:
    def maxRepOpt1(self, text: str) -> int:
        '''
        At least swap one character
        '''
        stack = [['!',0]]
        for i in text:
            if i != stack[-1][0]:
                stack += [[i,1]]
            else:
                stack[-1][1] += 1
        stack = stack[1:]
        res = 0
        cnt = collections.defaultdict(int)
        for i in stack:
            cnt[i[0]] += 1
        for i in range(1,len(stack)-1):
            if stack[i][1] == 1 and stack[i-1][0] == stack[i+1][0] and cnt[stack[i-1][0]] >= 3:
                res = max(res, stack[i-1][1]+stack[i+1][1]+1)
            if stack[i][1] == 1 and stack[i-1][0] == stack[i+1][0] and cnt[stack[i-1][0]] == 2:
                res = max(res, stack[i-1][1]+stack[i+1][1])
        for i in range(len(stack)):
            if cnt[stack[i][0]] >= 2:
                res = max(res, stack[i][1]+1)
            else:
                res = max(res, stack[i][1])
        #print(stack)
        return res
#
#         maxf = res = 0
#         temp = ''
#         count = collections.Counter()
#         for i in range(len(s) - 1):
#             if s[i] not in count:
#                 count[s[i]] += 1
#             else:
#                 if temp and s[i] != temp:
#                     if i >= 1 and s[i - 1] == s[i + 1] : count[s[i-1]] += 1
#                     else: 
#                         maxf = max(maxf, count[s[i-1]]) 
#                         count[s[i-1]] = 1

#                 count[s[i]] += 1
#             maxf = max(maxf, count[s[i]])
#             temp = s[i]
#         print(count)
#         return maxf