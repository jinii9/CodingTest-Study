def solution(k, tangerine):
    answer = 0
    a={}

    # > 1번 코드: tangerine에 담긴 각각 다른 종류의 사이즈별로 개수를 dict에 넣어줌.
    # ex) 1:3 2:5 3:1  -> 1은 3개, 2는 5개, 3은 1개
    for i in tangerine:
        if i in a:
            a[i]+=1
        else:
            a[i]=1

    # <체크용>
    print(a) # {1: 1, 2: 3, 3: 1, 5: 1}
    print(a.items()) # dict_items([(1, 1), (2, 3), (3, 1), (5, 1)])
    # -> dict_items([(키1, 값1), (키2, 값2), (키3, 값3), ...])
    print(list(a.items())) # [(1, 1), (2, 3), (3, 1), (5, 1)]

    # > 2번 코드: dict에 저장된 값들을 key값이 아닌 value 기준 내림차순 정렬
    # ex) key:value 일 때,  value가 많은 순으로 정렬 
    # (최소한의 종류를 출력하기 위해 많은 것들부터 상자에 담는다.)
    a = dict(sorted(a.items(), key=lambda x: x[1], reverse=True))
    
    # -> <sort함수 사용할 경우>
    # items = list(a.items())  # dict의 items를 리스트로 변환
    # items.sort(key=lambda x: x[1], reverse=True)  # value 기준 내림차순 정렬
    # a = dict(items)  # 정렬된 리스트를 다시 딕셔너리로 변환
    print(a) # {2: 3, 1: 1, 3: 1, 5: 1}
    
    # > 3번 코드: 내림차순 정렬된 value값을 k(상자에 담을 수 있는 귤 개수)에서 빼주면서 반복한다.
    # answer 값에 1씩 카운트해주며 (종류)
    # k가 0보다 작을때 (다 찼을 때) answer를 출력
    for i in a:
        print(i) # 2 1
        print(a[i]) # 3 1
        if k<=0:
            print("answer:", answer)
            return answer
        k-=a[i]
        answer+=1

    print("answer:", answer)
    return answer

solution(2, [1, 2, 2, 2, 3, 5])

####################################
# 참고 : https://velog.io/@minmong/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.2-%EA%B7%A4-%EA%B3%A0%EB%A5%B4%EA%B8%B0-Python-velog
# dict 활용
# 여기서는 마지막에 따로 변수를 사용하는게 아니라 k<=0이 될 때까지 빼기를 수행