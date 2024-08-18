from itertools import permutations

N = int(input())
arr = [list(input().split()) for _ in range(N)]
answer = 0

for per in permutations(range(1, 10), 3):
    ok = True

    for num, st, bl in arr:
        per_st = per_bl = 0

        for i in range(3):
            if str(per[i]) == num[i]:
                per_st += 1
            elif str(per[i]) in num:
                per_bl += 1

        if per_st != int(st) or per_bl != int(bl):
            ok = False
            break
    
    if ok:
        answer += 1

print(answer)