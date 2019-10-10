class Solution:
    def countVowelPermutation(self, n: int) -> int:
        end_with = {
            'a':1,
            'e':1,
            'i':1,
            'o':1,
            'u':1
        }
        
        while n > 1:
            tmp_end = {'a':0,'e':0,'i':0,'o':0,'u':0}
            for k in ['a','e','i','o','u']:
                if k == 'a': 
                    tmp_end['e'] += end_with[k]
                elif k == 'e':
                    tmp_end['a'] += end_with[k]
                    tmp_end['i'] += end_with[k]
                elif k == 'i':
                    tmp_end['a'] += end_with[k]
                    tmp_end['e'] += end_with[k]
                    tmp_end['o'] += end_with[k]
                    tmp_end['u'] += end_with[k]
                elif k == 'o':
                    tmp_end['i'] += end_with[k]
                    tmp_end['u'] += end_with[k]
                else:
                    tmp_end['a'] += end_with[k]
            for k in tmp_end.keys():
                end_with[k] = tmp_end[k]
            n -= 1
        
        return sum(end_with.values()) % (10 ** 9 + 7)