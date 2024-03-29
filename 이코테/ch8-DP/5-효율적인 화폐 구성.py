# 30분~
# 입력
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1) ## 리스트의 인덱스는 0부터 시작하므로, 금액 m에 해당하는 인덱스를 포함하기 위해 m + 1 길이의 리스트가 필요

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n): ## 화폐 단위 순회
    for j in range(array[i], m + 1): ## 모든 금액 대해 최소 화폐 개수 계산 - 현재 계산하고자 하는 금액 의미
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])

#############################################################
# 이거는 '점화식'을 봤는데도 처음에는 이해가 안갔다. 진짜 여러번 반복 필수!

# 화폐 단위에 따라, 2원이면 '현재 칸의 인덱스'와 '2칸 전의 인덱스에 2원을 더한 인덱스+1'을 비교를 해서 더 작은 값을 저장하는 방식으로 구현
## ex) 화폐 단위가 [1, 2, 5]이고, 만들고자 하는 금액이 11원이라고 가정
# 11원을 만들기 위해, 먼저 10원(11-1), 9원(11-2), 6원(11-5)을 만드는 최소 화폐 개수를 알아야 한다!
# 10원을 만드는 최소 화폐 개수에 1원짜리 화폐 1개를 더하면 11원을 만들 수 있다.
# 9원을 만드는 최소 화폐 개수에 2원짜리 화폐 1개를 더하면 11원을 만들 수 있다.
# 6원을 만드는 최소 화폐 개수에 5원짜리 화폐 1개를 더하면 11원을 만들 수 있다.
# 이 과정을 통해 각 경우에 대해 11원을 만드는 최소 화폐 개수를 계산할 수 있고, 그 중 가장 작은 값을 선택.

# dp 테이블
## d 인덱스 : 금액
## d 인덱스에 해당하는 값 : 금액을 만들기 위한 최소 화폐 개수
