# L개의 알파벳 : 최소 1개의 모음(aeiou) + 최소 2개의 자음
# 정렬 - 암호에서 증가하는 순서
# 문자의 종류 C가지 -> 가능성 있는 암호들을 구해라

# abc와 bac는 같은걸로 취급 -> 정렬해야하니까 

def combination(index, level):
    global L, C, S, choose, moeum
    check = False # 모음 체크
    count = 0 # 자음 체크

    if level == L:
        for x in choose:
            if x in moeum: # 최소 1개의 모음
                check = True
            if x not in moeum: # 최소 2개의 자음
                 count += 1

        if check and count > 1:
            choose.sort()
            print(''.join(choose))

        check = False # 백트래킹
        count = 0
        return
    

    for i in range(index, C):
        choose.append(S[i])
        combination(i+1, level+1)
        choose.pop()



L, C = map(int, input().split())
S = list(input().split())
S.sort()
choose = []
moeum = ['a', 'e', 'i', 'o', 'u']

combination(0, 0)



#############
# combination 라이브러리로도 풀이 가능





