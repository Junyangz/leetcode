class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        rf = 0
        c = collections.Counter(chars)
        for w in words:
            temp = collections.Counter(w)
            for k in temp.keys():
                if k not in c.keys() or c[k] < temp[k]:
                    break
            else:
                rf += len(w)
        return rf