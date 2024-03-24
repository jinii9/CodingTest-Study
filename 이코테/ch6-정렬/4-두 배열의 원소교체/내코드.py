# 45분 시작

# 입력
n, k = map(int, input().split())
aArr = list(map(int, input().split()))
bArr = list(map(int, input().split()))


# 1. 정렬
aArr.sort()
bArr.sort(reverse=True)

# 2. aArr의 첫번째와 bArr의 마지막 교체
for i in range(k): # k번 반복
    # aArr[i], bArr[i] = bArr[i], aArr[i]
    if aArr[i] < bArr[i]:
        aArr[i], bArr[i] = bArr[i], aArr[i]
    else: # bArr의 원소보다 작을 경우에만 원소를 교환하고, 그렇지 않으면 더 이상 교환하지 않고 반복문을 종료
        break

# count = 0
# for i in aArr:
#     count += i
# print(count)
print(sum(aArr)) # 배열 A의 모든 원소의 합을 출력


# 5 3
# 1 2 5 4 3
# 5 5 6 6 5

#########################################################
# [오답]
# aArr.append(map(int, input().split()))
# -> map 객체로 반환되어 리스트와는 다른 타입이므로 X

# for i in range(k): # k번 반복
# aArr[i], bArr[i] = bArr[i], aArr[i]
# -> bArr의 원소를 aArr로만 옮기는 것이 아니라, aArr와 bArr의 원소를 서로 교환하는 결과를 초래. 목적이 aArr의 합을 최대로 만드는 것이라면, bArr의 원소를 aArr로만 옮기려는 것이 더 적절

# count 변수
# -> sum() 함수 사용하기
