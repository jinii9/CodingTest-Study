# 스택 사용
# () 짝을 이루면 pop
# ()()
# (())()
# )()(
# (()(
def solution(s):
    answer = True
    
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else: # i == ')'
            # 처음에 ) 나올 경우
            if stack == []:
                return False
            else: #스택 안에 '('가 있고 ')'가 들어와 올바른 괄호 
                stack.pop()
    
    if stack != []:
        return False
    
    return True