# k개 중 6개 고르기
# 집합 S (오름차순)

# 순서 X음 => C


def combination(index, level):
    global S, k, arr

    if level == 6:
        # arr.sort()
        # answer = ' '.join(map(str, arr))
        # print(answer)
        for i in arr:
             print(i, end=' ')
        print()
        return 

    for i in range(index, k):
        arr.append(S[i])
        combination(i + 1, level + 1)
        arr.pop()

while True:
        arr = []
        S = list(map(int, input().split()))
        k = S.pop(0)

        if k == 0:
            break

        combination(0, 0)
        print()


# 라이브러리 사용
# from itertools import combinations

# while True:
# 	I = list(map(int, input().split()))

# 	k = I[0]
# 	arr = I[1:]
# 	if k == 0:
# 		break

# 	for comb in combinations(arr, 6):
# 		# comb : (1, 2, 3, 4, 5, 6) ...
# 		for u in comb:
# 			print(u, end=' ')
# 		print()
# 	print()