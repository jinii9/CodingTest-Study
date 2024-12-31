# N 동굴의 길이
# H 높이
# 개똥이가 파괴해야하는 장애물의 최솟값
# 그 구간이 총 몇 개 있는지

# solve
# 브루트포스 : H * N = 500,000 * 200,000 -> 시간초과

# 이진탐색 : 정렬.. 
# tops, bottoms 분리
# sort 정렬
# bottoms : 1 2 3 3 3 3 4 / tops : 2 2 3 3 3 4 4
# tops: 4 4 3 3 3 2 2
# ex) 높이 = 3일 때 파괴해야 하는 장애물 개수
# bottoms에서는 h 이상인데 가장 왼쪽, tops에서는 h 이하인데 가장 오른쪽
# bottoms : 전체 H - h 미만인 가장 오른쪽 구하기
# tops : h 이하인데 가장 오른쪽 구하기

import sys
input = lambda: sys.stdin.readline().rstrip()

def binary_search(arr, num):
    cur = -1
    step = len(arr)

    while step != 0:
        while (cur + step < len(arr) and arr[cur + step] <= num):
            cur += step
        step //= 2
    
    return cur


N, H = map(int, input().split())

# 바닥/천장 장애물 높이
bottoms = []
tops = []

for i in range(N):
    num = int(input())
    if i % 2 == 0: # 짝수
        bottoms.append(num)
    else:
        # tops.append(num)
        tops.append(H - num + 1)

# 정렬
bottoms = sorted(bottoms)
tops = sorted(tops)

# solve
answer_minValue = int(1e12)
answer_count = 0
for h in range(1, H+1): # 높이 1부터
    count_bottom = (N//2) - (binary_search(bottoms, h-1) + 1)
    count_top = binary_search(tops, h) + 1

    if answer_minValue == count_bottom + count_top:
        answer_count += 1
    if answer_minValue > count_bottom + count_top:
        answer_minValue = count_bottom + count_top
        answer_count = 1

print(answer_minValue, answer_count)



