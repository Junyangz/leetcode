class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # easy but not good solution
        ret = []

        def f(s):
            return collections.Counter(s)[sorted(s)[0]]

        fq, fw = [f(q) for q in queries], [f(w) for w in words]

        for v in fq:
            for i, w in enumerate(sorted(fw)):
                if v < w: 
                    ret.append(len(fw) - i)
                    break
            else:
                ret.append(0)
        return ret

        #f = sorted(w.count(min(w)) for w in words)
        #return [len(f) - bisect.bisect(f, q.count(min(q))) for q in queries]