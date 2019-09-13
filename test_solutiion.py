def solution(Parentheses):
    stack = []
    for s in Parentheses:
        if s != '0':
            if s != '(' and stack:
                if stack[-1] == '(': stack.pop() 
            else:
                stack.append(s)
        else:
            break

    return len(stack)