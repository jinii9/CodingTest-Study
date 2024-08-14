def permutation(level):
    global N, choose, check

    if level == N:
        for x in choose:
            print(x, end=' ')
        print()

    for i in range(1, N+1):
        if check[i] == True:
            continue

        check[i] = True
        choose.append(i)
        permutation(level+1)   
        check[i] = False
        choose.pop() 


N = int(input())
choose = []
check = [False] * (N+1)

permutation(0)


# 라이브러리 사용
# from itertools import permutations


# N = int(input())

# for permutation in permutations(range(1, N + 1), N):
#     print(' '.join(map(str, permutation)))