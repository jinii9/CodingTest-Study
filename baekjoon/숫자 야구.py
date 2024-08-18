# 21~
# 영수: 1~9 서로 다른 숫자 3개
# 동일한 위치 - 스트라이크
# 다른 자리에 위치 - 볼
# 3스타라이크 정답

# 영수가 생각하고 있을 가능성 있는 수가 총 몇 개인지 맞취기
# 민혁이가 질문한 세자리 수, 스트라이크 개수, 볼의 개수


##
# 1 2 3 4 8 9
# 1,123    1,356    2,327

from itertools import permutations

N = int(input())
arr = [ list(map(int, input().split())) for _ in range(N) ]
count = 0
answer = 0

for permutation in permutations(range(1, 10), 3):
    for x in arr:
        strike_count = 0
        ball_strike = 0

        for i, per in enumerate(permutation):
            # 스트라이크
            if per == int(str(x[0])[i]):
                strike_count += 1  
            # 볼
            if str(per) in str(x[0]):
                ball_strike += 1

        ball_strike -= strike_count
        if x[1]==strike_count and x[2]==ball_strike:
            count += 1
        else:
            break
    
    if count == N:
        # answer.append(permutation)
        answer += 1
    
    count = 0


print(answer)