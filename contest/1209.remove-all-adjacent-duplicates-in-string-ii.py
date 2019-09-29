class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for e in s:
            if stack != [] and stack[-1][0] == e:
                    stack[-1][1] += 1
            else:
                stack.append([e, 1])

            while stack and stack[-1][1] == k:
                stack.pop()
        
        return "".join([s[0] * s[1] for s in stack])