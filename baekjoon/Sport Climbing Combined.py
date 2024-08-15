# 리드 / 스피드 / 볼더링
# (1, 5, 2) = 10 곱
# 곱한 점수가 낮은 순 
# 곱한 점수가 같다면 합산 점수가 낮은 선수가 이긴다.
# 곱한 점수, 함산점수가 같다면 등번호가 낮은 선수가 이긴다.

# n 선수 수
# 등번호, 리드, 스피드, 볼더링

# 출력 : 금 은 동

n = int(input())
members = [list(map(int, input().split())) for _ in range(n)]

members = sorted(members, key=lambda x: (x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]))


# print(members[0][0], members[1][0], members[2][0])

for b, p, q, r in members[:3]:
    print(b, end=' ')