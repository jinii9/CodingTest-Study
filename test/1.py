# lotte
v = [[1, 2], [1, 3], [2, 3]]  # 예시 입력
sameX = v[0][0]
sameY = v[0][1]
for a, i in enumerate(v):
    if sameX == i[0]:
        sameX = i[0]
        print(sameX)
    elif sameX != i[0] and a < len(v)-1: # 1
        sameX - v[i+1][0]
        print(sameX)
    # else sameY == i[1]:
    #     sameY = i[1]

print(sameX)
# print (sameY)
# return answer

# answer를 반환하는 로직이 필요한 경우, 여기에 추가하세요.
# 예: answer.append(something)
# return answer