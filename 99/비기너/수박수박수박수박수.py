# 3 수박수
# 1수 2박 3수
# 4 수박수박
# 1수 2박 3수 4박
# 5 수박수박수
def solution(n):
    answer = ''
    a = "수"
    b = "박"
    count = 1
    while count != (n + 1):
        if count % 2 != 0:  # 홀
            answer += a  # 수
        else:  # 짝
            answer += b  # 박
        count += 1

    print(answer)

    return answer