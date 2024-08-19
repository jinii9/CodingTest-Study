# 최소 걸음 수 계산
# 한 번에 최대 M권

# 현재 0
# N 책의 개수
# M 한 번에 들 수 있는 책의 개수


# 브루트포스X
# 50 1 10000
# -10000 -999 .... 50개  .... 999 10000
# 10000!


# 7 2
# -39 -37 -29 -28 -6 (0) 2 11

# 마지막부터 or 처음부터?
# 왼쪽&처음 : 28+28 + 37+37 + 39
# 28 37 39 = 104
# 왼쪽&마지막 : 39+39 + 29+29 + 6
# 39 29 6 = 74
# => 마지막부터

# 2
# -1 3 4 5 6 11
# 4 6 11 = 21
# 11 5 3 = 19
# => 마지막부터



# 왼쪽 or 오른쪽 먼저?
# 왼쪽 오른쪽 숫자 비교
# 가장 큰 것끼리 비교
# 오른쪽이 더 큼

# 39 + 29+29 + 6+6 + 11 + 11 = 131



N, M = map(int, input().split())
location = list(map(int, input().split()))

location = sorted(location)
minus = [x for x in location if x < 0]
plus = [x for  x in location if x > 0]

# 음수 처리
minus_sum = 0
for i in range(0, len(minus), M):
    minus_sum += abs(minus[i])
minus_sum = minus_sum*2

# 양수 처리
plus_sum = 0
for i in range(len(plus)-1, -1, -M):
    plus_sum += plus[i]
plus_sum = plus_sum*2

# 마지막 돌아오는 부분 처리
answer = 0
if len(minus) > 0 and (len(plus) == 0 or abs(min(minus)) > max(plus)):
    answer = minus_sum + plus_sum - abs(min(minus))
else:
    answer = minus_sum + plus_sum - max(plus)

print(answer)
