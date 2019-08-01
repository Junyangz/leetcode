#
# @lc app=leetcode id=1106 lang=python3
#
# [1106] Parsing A Boolean Expression
#
class Solution:
    def parseBoolExpr(self, E: str) -> bool:
        o_stack = []
        b_stack = []
        
        def evalue(o, b):
            if o == '!': return not b[0]
            if o == '&': return all(b)
            if o == '|': return any(b)
            
        for e in E:
            if e in ['!', '&', '|']: o_stack.append(e)
            elif e != ',':
                if e == 't': b_stack.append(1)
                elif e == 'f': b_stack.append(0)
                elif e == ')':
                    temp = []
                    temp.append(b_stack.pop())
                    while temp[-1] != '(':
                        temp.append(b_stack.pop())
                    temp = temp[:-1]

                    if len(o_stack) == 1: return evalue(o_stack.pop(), temp)
                    else: b_stack.append(evalue(o_stack.pop(), temp))
                        
                else: b_stack.append(e)

            

