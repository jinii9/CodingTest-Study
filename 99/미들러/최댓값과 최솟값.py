# 6m
# 최소값 최대값

def solution(s):
    answer = ''

    min_num = min(list(map(int, s.split(' '))))
    max_num = max(list(map(int, s.split(' '))))
    
    answer = str(min_num) + ' ' + str(max_num)
    return answer