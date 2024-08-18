# 05~

# 인접해 이는 모든 문자가 같지 않은 문자열 = 행운
# 문자 재배치하면 서로 다른 행운의 문자열 몇 개?
# 원래 문자열 S도 행운의 문자열인지 체크


from itertools import permutations

def fact(x):
    if x == 0:
        return 1
    return fact(x-1) * x

S = input()
answer = 0

for perm in permutations(S):
    ok = True
    for i in range(0, len(S)-1):
        if perm[i] == perm[i+1]:
            ok = False
            break
    answer += ok

for i in range(ord('a'), ord('z')+1):
    answer //= fact(S.count(chr(i)))

print(answer)




# 메모리 초과
# from itertools import permutations

# S = input()
# answer = set()

# for x in permutations(S, len(S)):
#     ok = True

#     for i in range(len(x)-1):
#         if x[i] == x[i+1]:
#             ok = False
#             break


#     if ok:
#         answer.add(x)

# print(len(answer))





###
# def search(lev, st):
#     global S, answer

#     if lev == len(S):
#         ok = True
#         for i in range(len(st)-1):
#             if st[i] == st[i+1]:
#                 ok = False
        
#         if ok:
#             answer += 1
#         return
    

#     for i in range(len(S)):
#         search(lev + 1, st + S[i])
#         search(lev + 1, st[:-1])


# S = input()
# answer = 0
# search(0, '')
# print(answer)
