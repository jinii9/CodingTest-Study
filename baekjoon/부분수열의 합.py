# 22~
from itertools import combinations
N, S = map(int, (input().split()))
arr = list(map(int, input().split()))
answer = 0
for i in range(1, N+1):
    for com in combinations(arr, i):
        sum_value = 0
        for x in com:
            sum_value += x

        if sum_value == S:
            answer += 1

print(answer)