# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 44~14

answer = []
T = int(input())
for _ in range(T):
    special, general = map(int, input().split())
    # 상품으로 교환 가능한 최대 수를 계산
    possible_exchange = min(special // 5, (special + general) // 12)
    answer.append(possible_exchange)

for ans in answer:
    print(ans)

##############################################################################
# [해설 풀이]
# 1. 시즌 한정 쿠폰 사용 가능성
# 2. 일반 쿠폰 사용 가능성 : 일반 쿠폰만을 고려하는 것은 문제의 조건에 맞지 X으므로 패스
# 3. 총 쿠폰 사용 가능성

# [내 오답 풀이]
# special // 5 == 0이라면 0개
# special // 5 몫이 있다면 ok -> 나머지 keep
# general // 7 몫이 있다면 그만큼 special과 계산
# general // 7 == 0 이라면 special 몫과 나머지로 계산

# answer = []
# T = int(input())
# for i in range(T):
#     spetial, general = map(int, input().split())
#     spetial_value = 0
#     # spetial_temp = 0
#     general_value = 0
#     #
#     if spetial // 5 == 0:
#         answer.append(0)
#
#     else:
#         spetial_value = spetial // 5
#         # spetial_temp = spetial % 5
#
#         if general // 7 == 0:
#             answer.append(spetial // 12)
#         else:
#             general_value = general // 7
#             if spetial_value <= general_value:
#                 answer.append(spetial_value)
#             else:
#                 # 15개
#                 a = general_value
#                 b = spetial_value - general_value
#                 c = 0
#                 if b > 2:  # 15개 20개 25개
#                     c = b // 14
#
#                     answer.append(a + c)
#         # 2 3
#         # 3 5
#         # 7 3
#
# for i in range(T):
#     print(answer[i])

