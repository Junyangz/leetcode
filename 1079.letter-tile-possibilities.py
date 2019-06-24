#
# @lc app=leetcode id=1079 lang=python3
#
# [1079] Letter Tile Possibilities
#
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        #"AAB"
        #d = {s[:i] for s in itertools.permutations(tiles) for i in range(1,len(tiles) + 1)}
        #print(d)
        #'{(\'A\', \'B\'), (\'A\', \'B\', \'A\'), (\'A\',), (\'B\', \'A\'), (\'B\',), 
        # (\'B\', \'A\', \'A\'), (\'A\', \'A\'), (\'A\', \'A\', \'B\')}'
        return len({s[:i] for s in itertools.permutations(tiles) for i in range(1,len(tiles) + 1)})

