# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 입력 받기
N, K = map(int, input().split())

# 최소 선택 횟수 계산
# (N-1)을 (K-1)로 나눈 후, 나머지가 있으면 추가로 한 번 더 선택해야 함
min_selections = (N - 1) // (K - 1)
if (N - 1) % (K - 1) > 0:
    min_selections += 1

# 결과 출력
print(min_selections)

###################################################
# [정답 풀이]
# N-1은 첫 번째 숫자를 제외한 나머지 숫자들의 개수 (첫 번째 숫자는 어떠한 경우에도 최소 한 번은 선택되어야 하기 때문)
# K-1은 한 번에 선택할 수 있는 숫자들 중에서 실제로 위치를 변경할 수 있는 숫자들의 최대 개수
# 나눗셈의 결과에 나머지가 있는지 확인 필요 -> 나머지가 존재하는 경우, 이는 추가로 한 번 더 선택해야 한다는 것을 의미

# [내 오답 풀이]
# 정렬 -> slice로 배열 자르면서(변형하면서) count 세기
## 자꾸 3번 케이스가 불일치로 나왔다.
## 아직 왜 틀린지는 모르겠지만..
### 해당 문제는 연속된 숫자들을 선택하는 것에 초점을 맞추고 있지 않고, 모든 숫자를 커버하는 최소한의 선택 횟수를 찾는 것이라는 점!

# n, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort()
#
# count = 0
# first = data[0]
# while len(data) != 0:
#     if len(data) == k:
#         data = []
#         count += 1
#         break
#     elif len(data) > k - 1:  # 3
#         data[k - 1] = data[0]
#         data = data[k - 1:]  # 1 4
#         count += 1
#     # print(data)
#     else:
#         data = []
#         count += 1
#
# print(count)
