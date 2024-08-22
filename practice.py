# 동일한 자리에 위치 - 스트라이크
# 다른 자리에 위치 - 볼
# 324
# 429 : 1s 1b
# 241 : 0s 2b
# 924 : 2s 0b
# 3s이면 게임 끝


# 가능성 있는 수 개수 맞추기
# 질문수 N
# 수 S개수 B개수

# 브루트포스 : 100
# _ _ _ 9*8*7 = 9P3


# !! 120 130의 각 자릿수를 비교하기 위해서는 string이어야 한다 !!

from itertools import permutations

N = int(input())
arr = [input().split() for _ in range(N)]
answer = 0


for perm in permutations(range(1,10), 3):
    check = True

    for n, s, b in arr:
        b_count = s_count  = 0

        for i in range(3):
            if str(perm[i]) == n[i]:
                s_count += 1
            elif str(perm[i]) in n:
                b_count += 1

        if s_count != int(s) or b_count != int(b):
            check = False
            break
    
    if check:
        answer += 1

print(answer)