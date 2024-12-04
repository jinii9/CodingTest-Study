# N개의 회의실
# 각 회의 I - 시작시간, 끝시간
# 각 회의 겹치지 않게 사용할 수 있는 회의 최대 개수

# N 회의 수

# 브루트포스
# 시작시간을 기준으로 정렬
# N * 2^N
# 100,000 * 2^100,000


# 그리디
# 그리디와 정렬은 같이 쓰인다.
# 끝점을 기준으로 정렬

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
# meetings = [list(map(int, input().split())) for _ in range(N)]
times = []
for _ in range(N):
    s, e = map(int, input().split())
    times.append((s, e))


# meetings = sorted(meetings, key=lambda x: x[1])
times = sorted(times, key=lambda x: (x[1], x[0]))
# print(meetings)

answer = 0
end = 0
for s, e in times:
    if s >= end:
       end = e
       answer += 1 


print(answer)

